"""CR-01 reference solution: brute-force login detector."""
import ipaddress
import re
from collections import defaultdict
from datetime import datetime

_LINE = re.compile(r"(?P<ts>\S+)\s+FAILED_LOGIN\s+user=(?P<user>\S+)\s+ip=(?P<ip>\S+)")


def _parse(line):
    """Return (ip, epoch_seconds) for a valid failed-login line, else None."""
    match = _LINE.fullmatch(line.strip())
    if not match:
        return None
    try:
        timestamp = datetime.fromisoformat(match["ts"].replace("Z", "+00:00")).timestamp()
        ip = str(ipaddress.ip_address(match["ip"]))  # normalizes IPv6 spellings
    except ValueError:
        return None
    return ip, timestamp


def find_bruteforce_ips(lines, threshold, window_seconds):
    """Return sorted IPs with at least `threshold` failures inside any
    window of `window_seconds` seconds (window boundaries are inclusive)."""
    if threshold < 1 or window_seconds < 0:
        raise ValueError("threshold must be >= 1 and window_seconds >= 0")

    failures = defaultdict(list)
    for line in lines:
        parsed = _parse(line)
        if parsed is None:
            continue
        ip, timestamp = parsed
        failures[ip].append(timestamp)

    flagged = []
    for ip, times in failures.items():
        times.sort()
        left = 0
        for right in range(len(times)):
            while times[right] - times[left] > window_seconds:
                left += 1
            if right - left + 1 >= threshold:
                flagged.append(ip)
                break

    return sorted(flagged, key=lambda text: (ipaddress.ip_address(text).version, ipaddress.ip_address(text)))
