import java.io.StringReader;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;

/**
 * SV-04: XML import (vulnerable).
 *
 * A "notes" API accepts XML from clients and returns the text of the root
 * element. Review parseNote().
 */
public class VulnerableXmlParser {
    public static String parseNote(String xml) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        Document doc = factory.newDocumentBuilder().parse(new InputSource(new StringReader(xml)));
        return doc.getDocumentElement().getTextContent();
    }
}
