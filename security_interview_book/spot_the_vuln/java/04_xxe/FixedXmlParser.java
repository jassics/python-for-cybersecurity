import java.io.StringReader;
import javax.xml.XMLConstants;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;

/**
 * SV-04: XML import (one reasonable fix).
 *
 * DOCTYPE declarations are refused outright, which removes external entities
 * and entity-expansion tricks in one step. Secure processing and XInclude
 * settings are belt and braces.
 */
public class FixedXmlParser {
    public static String parseNote(String xml) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
        factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
        factory.setXIncludeAware(false);
        factory.setExpandEntityReferences(false);
        Document doc = factory.newDocumentBuilder().parse(new InputSource(new StringReader(xml)));
        return doc.getDocumentElement().getTextContent();
    }
}
