import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * SV-03: file download helper (vulnerable).
 *
 * A document portal serves files from a public directory. The file name
 * comes straight from the request. Review readFile().
 */
public class VulnerableFileServer {
    private final Path baseDir;

    public VulnerableFileServer(Path baseDir) {
        this.baseDir = baseDir;
    }

    public String readFile(String name) throws IOException {
        return Files.readString(baseDir.resolve(name));
    }
}
