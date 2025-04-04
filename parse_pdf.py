import json
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def fill_pdf_with_coordinates(json_file, template_pdf, output_dir):
    with open(json_file, 'r') as f:
        students = json.load(f)

    os.makedirs(output_dir, exist_ok=True)

    for student in students:
        original_pdf = PdfReader(template_pdf)
        output = PdfWriter()

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        student_name = student['student_name']
        student_id = student['student_id']
        grade_level = student['grade_level']

        # Draw text at specific coordinates
        # Note: Coordinates in points (72 points = 1 inch)
        # Origin (0,0) is at bottom left
        can.setFont('Helvetica', 10)
        can.drawString(126, 540, student_name)

        can.setFont("Helvetica", 14)
        can.drawString(375, 540, student_id)
        can.drawString(125, 518, grade_level)

        can.save()
        packet.seek(0)
        overlay_pdf = PdfReader(packet)
        page = original_pdf.pages[0]

        page.merge_page(overlay_pdf.pages[0])
        output.add_page(page)

        output_file = os.path.join(output_dir, f"{student['student_id']} Grade change form.pdf")
        with open(output_file, 'wb') as output_pdf:
            output.write(output_pdf)
        print(f"created {student_name}'s PDF")
    return f"created {len(students)} PDFs"
    

original_pdf = '/Users/ByrdBass/Documents/MAESTRO BYRD/MARIACHI/Rosters Mariachi/Grade_change_project/Grade Change form All signed.pdf'
output_path = '/Users/ByrdBass/Documents/MAESTRO BYRD/MARIACHI/Rosters Mariachi/Grade_change_project/finished_rosters'
fill_pdf_with_coordinates('student_data.json', original_pdf, output_path)