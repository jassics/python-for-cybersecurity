"""SV-02: user lookup helper (one reasonable fix).

No shell is involved: arguments are passed as a list, the input is validated
with an allowlist, and "--" stops grep from treating input as an option.
"""
import re
import subprocess

_USERNAME = re.compile(r"[A-Za-z0-9_.][A-Za-z0-9_.-]{0,31}")


def find_user(username: str, users_file: str) -> str:
    if not _USERNAME.fullmatch(username):
        raise ValueError("invalid username")
    result = subprocess.run(
        ["grep", "-F", "--", username, users_file],
        capture_output=True,
        text=True,
        check=False,  # grep exits 1 when nothing matches, which is not an error here
    )
    return result.stdout
