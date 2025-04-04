import json
import os
from PyPDF2 import PdfReader, PdfWriter

def check_pdf_type(pdf_path):
    reader = PdfReader(pdf_path)

    if reader.get_fields():
        print("This is an AcroForm PDF with the following fields")
        for field_name in reader.get_fields():
            print("=> "-{field_name})
        return "AcroForm"
    
    try:
        for page in reader.pages:
            if '/XFA' in page:
                print("This PDF uses XFA forms!  use different lib like pdftk or fillpdf")
    except:
        pass

    print("this PDF doesn't appear to have fillable fields \U0001F61E") #sadface
    return "Non-form"

check_pdf_type('/Users/ByrdBass/Documents/MAESTRO BYRD/MARIACHI/Rosters Mariachi/Grade_change_project/Grade Change form All signed.pdf')
