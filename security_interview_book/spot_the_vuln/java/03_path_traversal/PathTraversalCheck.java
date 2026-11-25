import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/** Plain-Java check (no test framework needed). Exits non-zero on failure. */
public class PathTraversalCheck {
    private static int failures = 0;

    interface Action {
        void run() throws Exception;
    }

    private static void check(String name, boolean ok) {
        System.out.println((ok ? "PASS  " : "FAIL  ") + name);
        if (!ok) {
            failures++;
        }
    }

    private static boolean blocked(Action action) {
        try {
            action.run();
            return false;
        } catch (SecurityException e) {
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public static void main(String[] args) throws Exception {
        Path root = Files.createTempDirectory("sv03");
        Path base = Files.createDirectory(root.resolve("public"));
        Files.writeString(base.resolve("hello.txt"), "hello");
        Files.writeString(root.resolve("secret.txt"), "TOP-SECRET");

        VulnerableFileServer vulnerable = new VulnerableFileServer(base);
        FixedFileServer fixed = new FixedFileServer(base);

        check("vulnerable serves a normal file", vulnerable.readFile("hello.txt").equals("hello"));
        check("vulnerable leaks ../secret.txt", vulnerable.readFile("../secret.txt").equals("TOP-SECRET"));
        check("vulnerable leaks an absolute path",
                vulnerable.readFile(root.resolve("secret.txt").toString()).equals("TOP-SECRET"));

        check("fixed serves a normal file", fixed.readFile("hello.txt").equals("hello"));
        check("fixed blocks ../secret.txt", blocked(() -> fixed.readFile("../secret.txt")));
        check("fixed blocks an absolute path",
                blocked(() -> fixed.readFile(root.resolve("secret.txt").toString())));

        try {
            Files.createSymbolicLink(base.resolve("link.txt"), root.resolve("secret.txt"));
            check("vulnerable follows a symlink out of the base", vulnerable.readFile("link.txt").equals("TOP-SECRET"));
            check("fixed blocks a symlink out of the base", blocked(() -> fixed.readFile("link.txt")));
        } catch (UnsupportedOperationException | IOException e) {
            System.out.println("SKIP  symlink checks (symlinks not available here)");
        }

        System.exit(failures == 0 ? 0 : 1);
    }
}
