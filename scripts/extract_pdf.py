import fitz
from PyPDF2 import PdfReader
from pathlib import Path

data= Path("../data")
pdf_files= data / "pdf_publication"

def extract_pdf():
    print(pdf_parse())


def pdf_parse():
    files= sorted(pdf_files.glob("*.pdf"))
    reader= PdfReader(files[0])
    return reader

if __name__=="__main__":
    extract_pdf()