from io import BytesIO, StringIO
from typing import Text

from pdfminer.converter import HTMLConverter, TextConverter 
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_html = BytesIO()
output_string = StringIO()


with open('docs/contracts/hotelier-sub.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = HTMLConverter(rsrcmgr, output_html, laparams=LAParams(line_overlap=0.1, line_margin=0.1, word_margin=0.05, char_margin=2.0))
    string_device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    string_interpreter = PDFPageInterpreter(rsrcmgr, string_device)

    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

    for page in PDFPage.create_pages(doc):
        string_interpreter.process_page(page)

print(output_html.getvalue().decode('utf8').replace("<body>", '<body style="text-align: justify;">'))
print(output_string.getvalue())
