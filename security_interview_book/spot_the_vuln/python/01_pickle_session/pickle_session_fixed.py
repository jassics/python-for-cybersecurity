"""SV-01: session cookie handling (one reasonable fix).

Data is serialized as JSON (a data-only format) and signed with HMAC-SHA256,
so the server only accepts cookies it issued itself.
"""
import base64
import hashlib
import hmac
import json


def _sign(key: bytes, payload: bytes) -> bytes:
    return hmac.new(key, payload, hashlib.sha256).digest()


def dump_session(session: dict, key: bytes) -> str:
    payload = json.dumps(session, separators=(",", ":"), sort_keys=True).encode()
    token = base64.urlsafe_b64encode(payload) + b"." + base64.urlsafe_b64encode(_sign(key, payload))
    return token.decode()


def load_session(cookie: str, key: bytes) -> dict:
    try:
        payload_b64, signature_b64 = cookie.encode().split(b".")
        payload = base64.urlsafe_b64decode(payload_b64)
        signature = base64.urlsafe_b64decode(signature_b64)
    except ValueError as exc:  # also covers base64 decoding errors
        raise ValueError("malformed session cookie") from exc

    if not hmac.compare_digest(signature, _sign(key, payload)):
        raise ValueError("invalid session signature")

    return json.loads(payload)
