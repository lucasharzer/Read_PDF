from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import os
import dotenv


def PDFToText(arquivo_pdf, arquivo_txt):

    inFile = open(arquivo_pdf, "rb")
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    txtConverter = TextConverter(resMgr, retData, laparams=LAParams())
    interpreter = PDFPageInterpreter(resMgr, txtConverter)
    for page in PDFPage.get_pages(inFile):
        interpreter.process_page(page)
    
    txt = retData.getvalue()

    with open(arquivo_txt, "w") as f:
        f.write(txt)


dotenv.load_dotenv(dotenv.find_dotenv())
arquivo_pdf = os.getenv("PDF_FILE")
arquivo_txt = os.getenv("TXT_FILE")

PDFToText(arquivo_pdf, arquivo_txt)
