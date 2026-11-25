# SV-04: XML import (Java)

**Book chapters:** 2 (OWASP web), 4 (secure code review) · **CWE-611:** Improper restriction of XML external entity reference · **Level:** mid

## Scenario

A notes API accepts XML from clients and returns the root element's text. The code uses the standard JDK parser and looks harmless. Review `VulnerableXmlParser.java`.

## Hints

<details>
<summary>Hint 1</summary>

XML has a feature that lets a document define its own entities. Where can an entity's value come from?
</details>

<details>
<summary>Hint 2</summary>

Which parser settings did the code change from the defaults? Which defaults are safe?
</details>

<details>
<summary>Hint 3</summary>

If the server cannot return the file contents to the client, can the attacker still use the bug?
</details>

## What the interviewer listens for

- You name the primitive: **external entities let the document make the server read files or fetch URLs**.
- You list the impact: local file read, SSRF (including cloud metadata endpoints), denial of service through entity expansion ("billion laughs").
- You know the fix is **parser configuration**, and that defaults differ by language and library. The robust fix is disallowing DOCTYPE entirely.
- You raise the other XML entry points: SOAP, SAML, SVG and Office document uploads, XML-based config.
- Blind XXE: out-of-band exfiltration still works when nothing is reflected.
- Senior bonus: whether XML is needed at all, or whether JSON would reduce the attack surface.

## The fix, explained

`FixedXmlParser.java` disables DOCTYPE declarations, turns on secure processing, and disables XInclude and entity expansion. The check shows the hostile document is refused and a normal one still parses.

The JDK prints a `[Fatal Error]` line to stderr when it refuses the DOCTYPE. That is the parser's default error handler, and it is expected output.

## The same bug elsewhere

| Language | Look for |
| --- | --- |
| Java | `DocumentBuilderFactory`, `SAXParserFactory`, `XMLInputFactory`, `TransformerFactory` with default settings |
| Python | `lxml` with `resolve_entities=True`, `xml.sax`, old `xmlrpc`; prefer `defusedxml` |
| .NET | `XmlDocument` and `XmlReader` with `DtdProcessing.Parse` |
| PHP | `libxml_disable_entity_loader` on old versions |
| Node.js | libxml bindings with `noent: true` |

## Desi analogy

An XML document is a form where, in the margin, you may write "copy the contents of the locked almirah here". A trusting clerk does it. The fix is a form with no margin.

## Run it

```bash
cd security_interview_book
mkdir -p build/04 && javac -d build/04 spot_the_vuln/java/04_xxe/*.java
java -cp build/04 XxeCheck
```

The hostile document only reads a temporary file the check creates itself.
