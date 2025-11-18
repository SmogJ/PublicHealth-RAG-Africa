import fitz
from PyPDF2 import PdfReader
from pathlib import Path

#   --- Directory of PDF files ---
data= Path("../data")
pdf_files= data / "pdf_publication"


#   --- Directory of extracted data ---
pdf_data= data / "pdf_data"
pdf_data.mkdir(exist_ok=True)

#    --- PDF DATA JSON File --- 
pdf_json= pdf_data / "pdf_publication.json"

def extract_pdf():

    #   --- get the PDF file name as a list and read the file one at time ---
    files= sorted(pdf_files.glob("*.pdf"))

    # --- Loop through the PDF files ---
    # for file in files:
    print(f"Extraxticng Data from PDF File: {files[0]}")
    with open(files[0], "rb") as pdf_file:
        reader= PdfReader(pdf_file)
        print(extract_data(reader))


def extract_data(reader):
    """
    Function extracts the content of a PDF file
    Input: PDF Reader 
    Return: Dictionary containing data
    """

    # --- Initializing Variables ---
    pdf_title= None
    pdf_author= None
    pdf_date= None
    pdf_info= None
    pdf_subject= None
    pdf_text= []

    
    # --- Get Pdf metadata ---
    pdf_pages= reader.pages
    num_pages= len(pdf_pages)
    pdf_metadata= reader.metadata
    pdf_author= pdf_metadata.author
    pdf_title= pdf_metadata.title
    pdf_date= pdf_metadata.creation_date
    pdf_info= pdf_metadata.producer
    pdf_subject= pdf_metadata.subject

    # --- Get Pdf text ---
    for num in range(num_pages):
        print(f"Extract Text from Page {num}")
        pdf_text.append(pdf_pages[num].extract_text())
    
    return {
        "pdf_author": pdf_author, 
        "pdf_title": pdf_title, 
        "pdf_date": pdf_date, 
        "num_pages": num_pages, 
        "pdf_info": pdf_info, 
        "pdf_subject": pdf_subject, 
        "pdf_text": pdf_text
    }

if __name__=="__main__":
    extract_pdf()