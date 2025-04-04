## setup
- create env
        
    `python3 -m venv excel_2_pdf_env`

- Activate the venv
    - MacOs and Linux 
        
        `source excel_2_pdf_env/bin/activate`

    - Windows
        
        `excel_2_pdf\Scripts\activate`

- Install dependencies

    `pip install pandas openpyxl PyPDF2 pdfrw reportlab`

- run the script for checking pdf type

    `python check_pdf_type.py`

- If no fields are found: run the script for checking pdf_coordinates

    `python create_pdf_coords.py`

