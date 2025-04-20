from fpdf import FPDF
import datetime
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)  # Revert to default Arial font
        self.cell(0, 10, "CyberAI Vulnerability Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)  # Revert to default Arial font
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)  # Revert to default Arial font
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 11)  # Revert to default Arial font
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_pdf_report(code, vulnerabilities, fixes, output_path="report.pdf"):
    pdf = PDFReport()

    # Revert to using the default font (Arial) to avoid the font issue
    pdf.set_font("Arial", "", 10)

    pdf.add_page()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(0, 10, f"Generated on: {timestamp}", ln=True)
    pdf.ln(5)

    pdf.add_section("Submitted Code", code)
    pdf.add_section("Vulnerability Analysis", vulnerabilities)
    pdf.add_section("Suggested Fixes", fixes)

    pdf.output(output_path)
    return output_path
