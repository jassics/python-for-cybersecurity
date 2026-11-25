"""SV-01: session cookie handling (vulnerable).

You are reviewing a pull request for a small web service. Sessions are kept
in a cookie so that no server-side storage is needed. How many problems can
you find?
"""
import base64
import pickle


def dump_session(session: dict) -> str:
    """Serialize the session into a cookie value."""
    return base64.urlsafe_b64encode(pickle.dumps(session)).decode()


def load_session(cookie: str) -> dict:
    """Rebuild the session from the cookie sent by the browser."""
    return pickle.loads(base64.urlsafe_b64decode(cookie))
