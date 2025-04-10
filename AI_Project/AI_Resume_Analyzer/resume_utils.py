import pdfplumber
def Extract_text(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
         text += page.extract_text()
        return text  
    