# SV-03: File download (Java)

**Book chapters:** 2 (OWASP web), 3 (API security), 4 (secure code review) · **CWE-22:** Path traversal · **Level:** junior to mid

## Scenario

A document portal serves files from a public directory. The file name arrives as a query parameter and goes straight into `readFile`. Review `VulnerableFileServer.java`.

## Hints

<details>
<summary>Hint 1</summary>

What does `Path.resolve` do when the argument contains `..`? What if the argument is an absolute path?
</details>

<details>
<summary>Hint 2</summary>

You decided to reject `..`. Does a string check on the input cover URL-encoded input, or paths that are valid only after the filesystem resolves them?
</details>

<details>
<summary>Hint 3</summary>

A user uploads a file named `link.txt` that is a symbolic link. Where does it point?
</details>

## What the interviewer listens for

- You explain that the vulnerability is **not** "the string contains dots", it is that the **resolved path leaves the base directory**.
- Your fix **canonicalizes first, then checks the prefix** (`normalize` plus `startsWith` on a real base path), rather than filtering strings.
- You mention symlinks and re-check after resolving them.
- You ask where else the name is used: logging, content-type guessing, storage keys.
- This is an authorization bug too. Ask: should this user be allowed to read this file at all? Name-based access without per-file ownership is IDOR.
- Senior bonus: serve files through opaque IDs instead of names, so the user never supplies a path.

## The fix, explained

`FixedFileServer.java` normalizes the joined path, requires it to start with the real base directory, resolves symlinks with `toRealPath`, and checks the prefix again.

## The same bug elsewhere

| Language | Look for |
| --- | --- |
| Python | `open(os.path.join(base, name))` (an absolute `name` replaces the base), `send_file`, `tarfile.extractall` |
| JavaScript | `path.join(base, req.query.name)`, `res.sendFile` without a `root` option |
| Go | `filepath.Join(base, name)` without a prefix check, `http.Dir` with unusual roots |
| PHP | `include $_GET["page"]`, `file_get_contents` |

## Desi analogy

"Bhaiya, give me the file from Room 12", and the clerk walks wherever the note says, including out the back door and into the manager's cabin. The check is not "does the note say *back door*", it is "where did the clerk end up standing?".

## Run it

```bash
cd security_interview_book
mkdir -p build/03 && javac -d build/03 spot_the_vuln/java/03_path_traversal/*.java
java -cp build/03 PathTraversalCheck
```

Or run everything with `make test-java`.
