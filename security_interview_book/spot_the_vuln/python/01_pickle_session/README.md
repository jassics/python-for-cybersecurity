# SV-01: Session cookie (Python)

**Book chapters:** 2 (OWASP web), 4 (secure code review) · **CWE-502:** Deserialization of untrusted data · **Level:** junior to mid

## Scenario

A pull request moves sessions from server-side storage into a cookie, "so we can scale without Redis". Read `pickle_session_vulnerable.py` and list every problem before opening the hints.

## Hints

<details>
<summary>Hint 1</summary>

Who controls the bytes passed to `pickle.loads`?
</details>

<details>
<summary>Hint 2</summary>

Pickle is not a data format. It is a small program that the unpickler executes. Look up `__reduce__`.
</details>

<details>
<summary>Hint 3</summary>

Even if the exploit did not exist, is there anything stopping a user from editing their own role inside the cookie?
</details>

## What the interviewer listens for

- You name remote code execution first, not "data tampering".
- You explain why: the attacker chooses the callable that runs during `loads`.
- You say that encryption or base64 does not help; **integrity** (a signature) does, and the signature must be checked **before** parsing.
- You prefer a data-only format (JSON) over pickle, even when signed.
- Senior bonus: key management and rotation, expiry in the payload, replay, and why a server-side session ID may be simpler than a signed cookie.

## The fix, explained

`pickle_session_fixed.py` switches to JSON and signs the payload with HMAC-SHA256. It compares signatures with `hmac.compare_digest` (constant time) and verifies before parsing. It is deliberately minimal: a real fix would also add an expiry and a key-rotation scheme.

## The same bug elsewhere

| Language | Look for |
| --- | --- |
| Python | `pickle.loads`, `yaml.load` without `SafeLoader`, `marshal.loads`, `jsonpickle.decode` |
| Java | `ObjectInputStream.readObject` on untrusted input (see gadget chains) |
| PHP | `unserialize()` |
| Ruby | `Marshal.load`, `YAML.load` |
| Node.js | `node-serialize` and similar libraries |
| Go | `encoding/gob` is type-restricted, but check any "decode into `interface{}`" pattern |

## Desi analogy

Accepting a tiffin from a stranger and following the note inside it that says "heat me with this stove". The note, not the food, is the problem.

## Run it

```bash
pytest spot_the_vuln/python/01_pickle_session
```

The test's "attacker code" only appends a message to a list. It never touches your system.
