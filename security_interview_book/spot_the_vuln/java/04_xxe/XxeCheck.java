import java.nio.file.Files;
import java.nio.file.Path;

/** Plain-Java check (no test framework needed). Exits non-zero on failure. */
public class XxeCheck {
    private static int failures = 0;

    private static void check(String name, boolean ok) {
        System.out.println((ok ? "PASS  " : "FAIL  ") + name);
        if (!ok) {
            failures++;
        }
    }

    public static void main(String[] args) throws Exception {
        Path secret = Files.createTempFile("sv04", ".txt");
        Files.writeString(secret, "TOP-SECRET-XXE");

        String hostile = "<?xml version=\"1.0\"?>"
                + "<!DOCTYPE note [<!ENTITY x SYSTEM \"" + secret.toUri() + "\">]>"
                + "<note>&x;</note>";
        String benign = "<note>hello</note>";

        check("vulnerable parses a normal note", VulnerableXmlParser.parseNote(benign).equals("hello"));
        check("vulnerable leaks a local file through an external entity",
                VulnerableXmlParser.parseNote(hostile).contains("TOP-SECRET-XXE"));

        check("fixed parses a normal note", FixedXmlParser.parseNote(benign).equals("hello"));
        boolean refused;
        try {
            FixedXmlParser.parseNote(hostile);
            refused = false;
        } catch (Exception e) {
            refused = true;
        }
        check("fixed refuses the hostile document", refused);

        Files.deleteIfExists(secret);
        System.exit(failures == 0 ? 0 : 1);
    }
}
