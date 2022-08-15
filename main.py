from io import BytesIO, StringIO
from typing import Text

from pdfminer.converter import HTMLConverter, TextConverter 
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def convert_pdf_to_html(path: Text) -> Text:
    output_html = BytesIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = HTMLConverter(rsrcmgr, output_html, laparams=LAParams(line_overlap=0.1, line_margin=0.1, word_margin=0.05, char_margin=2.0))
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return output_html.getvalue().decode('utf8').replace("<body>", '<body style="text-align: justify;">')

def convert_pdf_to_string(path: Text) -> Text:
    output_string = StringIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        string_device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        string_interpreter = PDFPageInterpreter(rsrcmgr, string_device)

        for page in PDFPage.create_pages(doc):
            string_interpreter.process_page(page)

    return output_string.getvalue()
