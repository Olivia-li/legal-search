from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_text_to_fp

output_string = StringIO()
output_string2 = StringIO()

with open('docs/contracts/groundfloor-sub.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

# print(output_string.getvalue())

with open ('docs/contracts/groundfloor-sub.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string2, laparams=LAParams(), output_type='html', codec=None)

print(output_string2.getvalue())