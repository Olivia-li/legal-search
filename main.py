from io import BytesIO, StringIO
from typing import Dict, Text
import re
from pdfminer.converter import HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def convert_pdf_to_html(path: Text, definitions: Dict) -> Text:
    output_html = BytesIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = HTMLConverter(rsrcmgr, output_html, laparams=LAParams(line_overlap=0.5, line_margin=0.1, char_margin=2.0))
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    output_html = output_html.getvalue().decode('utf8')
    for key, value in definitions.items():
        output_html = re.sub(key, f"<span id='{value}'>{key}</span>", output_html, flags=re.IGNORECASE)
    return(output_html)


def convert_pdf_to_string(path: Text) -> Text:
    output_string = StringIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        string_device = TextConverter(rsrcmgr, output_string, laparams=LAParams(line_margin=4.0))
        string_interpreter = PDFPageInterpreter(rsrcmgr, string_device)

        for page in PDFPage.create_pages(doc):
            string_interpreter.process_page(page)

    return output_string.getvalue()

# convert_pdf_to_html("docs/contracts/groundfloor-sub.pdf")
# convert_pdf_to_string("docs/contracts/groundfloor-sub.pdf")
