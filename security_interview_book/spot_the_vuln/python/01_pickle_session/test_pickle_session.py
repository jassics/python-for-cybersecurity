import base64
import pickle

import pytest

import pickle_session_fixed as fixed
import pickle_session_vulnerable as vulnerable

KEY = b"test-only-secret-key-do-not-reuse"

# Stand-in for attacker code. A real attacker would call something like
# os.system here; we only record that the call happened.
EXPLOIT_LOG = []


def record_exploit(message):
    EXPLOIT_LOG.append(message)


class Forged:
    def __reduce__(self):
        return (record_exploit, ("code ran during deserialization",))


def forged_cookie() -> str:
    return base64.urlsafe_b64encode(pickle.dumps(Forged())).decode()


@pytest.fixture(autouse=True)
def clear_log():
    EXPLOIT_LOG.clear()


def test_vulnerable_round_trip_works():
    cookie = vulnerable.dump_session({"user": "alice"})
    assert vulnerable.load_session(cookie) == {"user": "alice"}


def test_vulnerable_runs_attacker_code():
    vulnerable.load_session(forged_cookie())
    assert EXPLOIT_LOG == ["code ran during deserialization"]


def test_fixed_round_trip_works():
    cookie = fixed.dump_session({"user": "alice", "role": "user"}, KEY)
    assert fixed.load_session(cookie, KEY) == {"user": "alice", "role": "user"}


def test_fixed_rejects_forged_pickle_cookie():
    with pytest.raises(ValueError):
        fixed.load_session(forged_cookie(), KEY)
    assert EXPLOIT_LOG == []


def test_fixed_rejects_tampered_payload():
    cookie = fixed.dump_session({"user": "alice", "role": "user"}, KEY)
    _, signature = cookie.split(".")
    evil_payload = base64.urlsafe_b64encode(b'{"role":"admin","user":"alice"}').decode()
    with pytest.raises(ValueError):
        fixed.load_session(f"{evil_payload}.{signature}", KEY)


def test_fixed_rejects_wrong_key():
    cookie = fixed.dump_session({"user": "alice"}, KEY)
    with pytest.raises(ValueError):
        fixed.load_session(cookie, b"a-different-key")
