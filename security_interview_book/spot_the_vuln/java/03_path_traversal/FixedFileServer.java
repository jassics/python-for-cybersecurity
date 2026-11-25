import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * SV-03: file download helper (one reasonable fix).
 *
 * The requested path is normalized and must stay inside the base directory.
 * It is checked a second time after symlinks are resolved.
 */
public class FixedFileServer {
    private final Path baseDir;

    public FixedFileServer(Path baseDir) {
        this.baseDir = baseDir;
    }

    public String readFile(String name) throws IOException {
        Path base = baseDir.toRealPath();
        Path target = base.resolve(name).normalize();
        if (!target.startsWith(base)) {
            throw new SecurityException("path escapes base directory");
        }
        Path real = target.toRealPath();
        if (!real.startsWith(base)) {
            throw new SecurityException("path escapes base directory via symlink");
        }
        return Files.readString(real);
    }
}
