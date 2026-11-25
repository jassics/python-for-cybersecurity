import pytest

import shell_injection_fixed as fixed
import shell_injection_vulnerable as vulnerable


@pytest.fixture
def users_file(tmp_path):
    path = tmp_path / "users.txt"
    path.write_text("alice,admin\nbob,support\n")
    return str(path)


def test_vulnerable_normal_lookup_works(users_file):
    assert "alice,admin" in vulnerable.find_user("alice", users_file)


def test_vulnerable_allows_command_injection(users_file):
    output = vulnerable.find_user("alice; echo INJECTED", users_file)
    assert "INJECTED" in output  # the attacker's command ran


def test_fixed_normal_lookup_works(users_file):
    assert "alice,admin" in fixed.find_user("alice", users_file)


def test_fixed_no_match_returns_empty(users_file):
    assert fixed.find_user("carol", users_file) == ""


@pytest.mark.parametrize(
    "payload",
    ["alice; echo INJECTED", "alice | echo INJECTED", "$(echo INJECTED)", "`echo INJECTED`", "-v", ""],
)
def test_fixed_rejects_hostile_input(users_file, payload):
    with pytest.raises(ValueError):
        fixed.find_user(payload, users_file)
