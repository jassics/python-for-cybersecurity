"""SV-02: user lookup helper (vulnerable).

An internal admin tool lets support staff search a users file by name.
Review the function below.
"""
import subprocess


def find_user(username: str, users_file: str) -> str:
    """Return the lines of users_file that match username."""
    command = f"cat {users_file} | grep {username}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
