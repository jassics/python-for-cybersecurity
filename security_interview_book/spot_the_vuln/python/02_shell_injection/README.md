# SV-02: User lookup helper (Python)

**Book chapters:** 2 (OWASP web), 4 (secure code review) · **CWE-78:** OS command injection · **Level:** junior to mid

## Scenario

An internal support tool lets staff search a users file by name. The function below is called from an admin web page. Find the vulnerabilities in `shell_injection_vulnerable.py`.

## Hints

<details>
<summary>Hint 1</summary>

What does `shell=True` do with the whole string?
</details>

<details>
<summary>Hint 2</summary>

Try the input `alice; echo INJECTED`. What does the shell see?
</details>

<details>
<summary>Hint 3</summary>

Is the file path trusted? Where does it come from in the real application?
</details>

## What the interviewer listens for

- You identify shell metacharacters (`;`, `|`, `&&`, `$(...)`, backticks) and say what the attacker gains: arbitrary commands as the service user.
- You say **avoid the shell** (argument list) before you say **sanitize**.
- You use an **allowlist** for the username, not a blocklist of bad characters.
- You know the second-order issue: a value starting with `-` becomes an option to the program. `--` fixes that.
- You ask whether a subprocess is needed at all: reading and filtering a file is a few lines of pure Python.
- Senior bonus: least privilege for the service account, and logging of the command for detection.

## The fix, explained

`shell_injection_fixed.py` validates the input against a strict pattern, then calls `grep` with an argument list (no shell) and `--`. Replacing the call with plain Python file reading would be even better.

## The same bug elsewhere

| Language | Look for |
| --- | --- |
| Python | `os.system`, `subprocess` with `shell=True`, `os.popen` |
| Java | `Runtime.exec(String)` building a command from input, `ProcessBuilder("sh", "-c", ...)` |
| JavaScript | `child_process.exec`, template strings passed to a shell |
| Go | `exec.Command("sh", "-c", ...)` |
| Ruby, PHP, Perl | backticks, `system()`, `shell_exec()` |

## Desi analogy

You tell the auto driver your destination and he hears "...and stop at my cousin's shop on the way". Passing arguments as a list is writing the address on a card the driver cannot reinterpret.

## Run it

```bash
pytest spot_the_vuln/python/02_shell_injection
```

The injected command is just `echo`.
