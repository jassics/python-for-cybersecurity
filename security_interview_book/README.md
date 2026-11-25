# Security Interview Book: Companion Exercises

Runnable exercises for the **Product Security Interview Playbook** (Vol 1: Fundamentals, Vol 2: Scenarios, Spot-the-Vuln and Coding Round). Chapter numbers in the book match the exercise numbers here.

> **Warning: this folder contains intentionally vulnerable code.**
> Every `*_vulnerable.*` / `Vulnerable*.java` file exists to be read, broken in a test and fixed.
> Never deploy it, never import it into a real project, and expect code scanners to flag it.
> The tests only touch temporary files and harmless marker functions. No exploit here does anything outside its own test run.

## How each exercise works

Each exercise folder has the same shape:

| File | Purpose |
| --- | --- |
| `README.md` | The scenario, hints, what an interviewer listens for, the fix explained, and the same bug in other languages |
| `*_vulnerable.*` | The code you are asked to review |
| `*_fixed.*` | One reasonable fix |
| test / check file | Proves the exploit works on the vulnerable version and fails on the fixed one |

Suggested way to practise: read only the vulnerable file, write down every issue you can find, then open the README hints, then run the tests.

## Exercises in this pilot

| ID | Language | Bug | CWE | Book chapter |
| --- | --- | --- | --- | --- |
| SV-01 | Python | Insecure deserialization of a session cookie | CWE-502 | 2, 4 |
| SV-02 | Python | OS command injection via `shell=True` | CWE-78 | 2, 4 |
| SV-03 | Java | Path traversal in a file download | CWE-22 | 2, 3, 4 |
| SV-04 | Java | XML external entity (XXE) | CWE-611 | 2, 4 |
| SV-05 | JavaScript | Prototype pollution in a deep merge | CWE-1321 | 2, 4 |
| CR-01 | Python | Coding round, tier 1: brute-force login detector | none | 12 |

## Running

Requirements: Python 3.11+, JDK 17+ (21 recommended), Node.js 18+.

```bash
cd security_interview_book
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

make test          # everything
make test-python   # SV-01, SV-02, CR-01
make test-java     # SV-03, SV-04
make test-js       # SV-05
```

To practise a coding-round problem, implement it in the stub file named in that problem's README and run the tests against your file:

```bash
IMPL=bruteforce_detector pytest coding_round/tier1_bruteforce_detector
```

## Related repositories

- [security-study-plan](https://github.com/jassics/security-study-plan): domain-by-domain study checklists
- [security-interview-questions](https://github.com/jassics/security-interview-questions): conceptual and scenario question banks

This folder adds the part those two do not cover: code you can run, break and fix.
