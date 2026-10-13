from fpdf import FPDF
from PIL import Image


def main():
    pdf = FPDF()
    inp = input("Name: ") + " took CS50"
    pdf = FPDF(orientation='P', unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Times", style="B", size=55)
    pdf.cell(0, 40, "CS50 Shirtificate", align='C')
    pdf.image("shirtificate.png", x=(210 - 190) / 2, y=65, w=190)
    pdf.set_x((210 - 190) / 2)
    pdf.set_y(115)
    pdf.set_font("Times", style="B", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 40, inp, align='C')
    pdf.output("shirtificate.pdf")


main()
