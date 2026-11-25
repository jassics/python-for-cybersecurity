import importlib
import os

import pytest

impl = importlib.import_module(os.environ.get("IMPL", "bruteforce_detector_solution"))
find = impl.find_bruteforce_ips


def failed(second, ip, user="alice", minute=0):
    return f"2026-11-25T10:{minute:02d}:{second:02d}Z FAILED_LOGIN user={user} ip={ip}"


def test_flags_ip_with_enough_failures_in_window():
    lines = [failed(s, "203.0.113.9") for s in (0, 10, 20)]
    assert find(lines, threshold=3, window_seconds=30) == ["203.0.113.9"]


def test_ignores_ip_below_threshold():
    lines = [failed(s, "203.0.113.9") for s in (0, 10)]
    assert find(lines, threshold=3, window_seconds=30) == []


def test_window_boundary_is_inclusive():
    lines = [failed(0, "198.51.100.1"), failed(15, "198.51.100.1"), failed(30, "198.51.100.1")]
    assert find(lines, threshold=3, window_seconds=30) == ["198.51.100.1"]
    assert find(lines, threshold=3, window_seconds=29) == []


def test_failures_spread_out_do_not_count():
    lines = [failed(0, "203.0.113.9", minute=m) for m in (0, 10, 20, 30)]
    assert find(lines, threshold=3, window_seconds=60) == []


def test_unsorted_input_is_handled():
    lines = [failed(20, "203.0.113.9"), failed(0, "203.0.113.9"), failed(10, "203.0.113.9")]
    assert find(lines, threshold=3, window_seconds=30) == ["203.0.113.9"]


def test_each_ip_is_counted_separately():
    lines = [failed(0, "203.0.113.9"), failed(1, "198.51.100.1"), failed(2, "203.0.113.9")]
    assert find(lines, threshold=2, window_seconds=10) == ["203.0.113.9"]


def test_results_sorted_numerically_not_alphabetically():
    lines = [failed(0, "10.0.0.9"), failed(1, "10.0.0.9"), failed(0, "10.0.0.10"), failed(1, "10.0.0.10")]
    assert find(lines, threshold=2, window_seconds=5) == ["10.0.0.9", "10.0.0.10"]


def test_malformed_lines_are_skipped():
    lines = [
        "garbage",
        "",
        "2026-13-45T99:99:99Z FAILED_LOGIN user=alice ip=203.0.113.9",
        "2026-11-25T10:00:00Z FAILED_LOGIN user=alice ip=not-an-ip",
        "2026-11-25T10:00:00Z SUCCESS_LOGIN user=alice ip=203.0.113.9",
        failed(0, "203.0.113.9"),
        failed(1, "203.0.113.9"),
    ]
    assert find(lines, threshold=2, window_seconds=5) == ["203.0.113.9"]


def test_log_injection_in_username_does_not_create_events():
    hostile = "2026-11-25T10:00:00Z FAILED_LOGIN user=bob ip=198.51.100.7 extra FAILED_LOGIN user=x ip=203.0.113.9"
    assert find([hostile], threshold=1, window_seconds=5) == []


def test_ipv6_spellings_count_as_one_address():
    lines = [failed(0, "2001:db8::1"), failed(1, "2001:0db8:0000:0000:0000:0000:0000:0001")]
    assert find(lines, threshold=2, window_seconds=5) == ["2001:db8::1"]


def test_empty_input():
    assert find([], threshold=1, window_seconds=10) == []


@pytest.mark.parametrize("threshold,window", [(0, 10), (-1, 10), (3, -5)])
def test_invalid_parameters_raise(threshold, window):
    with pytest.raises(ValueError):
        find([], threshold=threshold, window_seconds=window)
