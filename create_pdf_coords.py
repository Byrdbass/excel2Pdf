import json
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_coordinate_grid(pdf_path, output_path):
    """Create a coordinate grid overlay to help find positions on the PDF."""
    # Get the existing PDF
    original_pdf = PdfReader(pdf_path)
    output = PdfWriter()
    
    # Get the dimensions of the first page
    page = original_pdf.pages[0]
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)
    
    # Create a new PDF with a coordinate grid
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(width, height))
    
    # Draw grid lines every 50 points
    can.setStrokeColorRGB(0.7, 0.7, 0.7)  # Light gray
    can.setFont("Helvetica", 8)
    
    # Draw horizontal lines and y-coordinates
    for y in range(0, int(height), 50):
        can.line(0, y, width, y)
        can.drawString(5, y+2, str(y))
    
    # Draw vertical lines and x-coordinates
    for x in range(0, int(width), 50):
        can.line(x, 0, x, height)
        can.drawString(x+2, 5, str(x))
    
    # Save the canvas
    can.save()
    packet.seek(0)
    
    # Create overlay PDF
    overlay_pdf = PdfReader(packet)
    
    # Merge with original
    page.merge_page(overlay_pdf.pages[0])
    
    # For newer PyPDF2 versions
    output.add_page(page)
    
    # Write output
    with open(output_path, 'wb') as output_file:
        output.write(output_file)
    
    return f"Created coordinate grid at {output_path}"

original_pdf = '/Users/ByrdBass/Documents/MAESTRO BYRD/MARIACHI/Rosters Mariachi/Grade_change_project/Grade Change form All signed.pdf'
output_path = '/Users/ByrdBass/Documents/MAESTRO BYRD/MARIACHI/Rosters Mariachi/Grade_change_project'

create_coordinate_grid(original_pdf, 'coordinate_grid.pdf')

    # Once you've identified the coordinates, run this:
    # result = fill_pdf_with_coordinates("students.json", "Grade Change form All signed.pdf", "completed_forms")
    # print(result)