# CR-01: Brute-force login detector

**Book chapter:** 12 (coding round) · **Tier:** 1 (warm-up, 20 to 25 minutes) · **Level:** junior to mid · **Language:** Python

## Problem

You receive authentication log lines in this format:

```
2026-11-25T10:00:03Z FAILED_LOGIN user=alice ip=203.0.113.9
```

Write `find_bruteforce_ips(lines, threshold, window_seconds)` that returns the sorted list of IP addresses with **at least `threshold` failed logins inside any window of `window_seconds` seconds** (both ends of the window are inclusive).

Rules:

- Lines may be out of order.
- Lines that do not match the format, or have an invalid timestamp or IP, are skipped. Never crash on bad input.
- Only `FAILED_LOGIN` lines count.
- Different spellings of the same IPv6 address are the same address.
- Sort IPv4 before IPv6, and numerically inside each (so `10.0.0.9` comes before `10.0.0.10`).
- `threshold < 1` or `window_seconds < 0` raise `ValueError`.

Example:

```python
lines = [
    "2026-11-25T10:00:00Z FAILED_LOGIN user=alice ip=203.0.113.9",
    "2026-11-25T10:00:10Z FAILED_LOGIN user=bob ip=203.0.113.9",
    "2026-11-25T10:00:20Z FAILED_LOGIN user=carol ip=203.0.113.9",
]
find_bruteforce_ips(lines, threshold=3, window_seconds=30)  # ["203.0.113.9"]
```

## How to practise

1. Implement it in `bruteforce_detector.py`.
2. Run `IMPL=bruteforce_detector pytest coding_round/tier1_bruteforce_detector`.
3. Only then open `bruteforce_detector_solution.py`.

Say your plan out loud before you code. That is half of what is being scored.

## Hints

<details>
<summary>Hint 1: structure</summary>

Group timestamps per IP first. Each IP is then an independent problem.
</details>

<details>
<summary>Hint 2: the window</summary>

Sort each IP's timestamps. For each timestamp, how many earlier timestamps are within `window_seconds`? A moving left pointer avoids rescanning.
</details>

<details>
<summary>Hint 3: input handling</summary>

Parse with a strict regex and `fullmatch`, then validate the timestamp and the IP with the standard library. Do not invent your own IP parsing.
</details>

## What the interviewer listens for

- You clarify before coding: window inclusivity, ordering, what "bad line" means, volume of data.
- You state complexity: O(n log n) from sorting, O(n) memory.
- You handle hostile input on purpose. A log line is attacker-influenced data (usernames can contain spaces and fake fields). The strict regex with `fullmatch` means a line with extra injected fields creates no event.
- You test edge cases yourself: boundary of the window, threshold 1, empty input, IPv6.
- You separate parsing from detection, so each part is testable.

## Follow-up questions

- The logs are 50 GB. How do you process them? (Stream, bucket by IP, bound memory with a deque per IP.)
- You must alert in real time. What changes? (A per-IP sliding window with expiry, plus a cap on tracked IPs.)
- Attackers rotate IPs and spray one password across many users. What would you detect instead? (Failures per user across IPs, or per password attempt pattern.)
- Legitimate users behind one corporate NAT look like one IP. How do you avoid blocking them?
- How would you explain this code to a reviewer if an AI assistant wrote the first draft? What would you check first?

## Complexity

Time O(n log n), space O(n) for n valid lines. The reference solution is in `bruteforce_detector_solution.py`.
