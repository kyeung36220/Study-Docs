from fpdf import FPDF, Align


class PDF():
    def __init__(self, name):
        pdf = FPDF(orientation="P")
        pdf.add_page()
        pdf.set_font("helvetica", style="B", size=48)
        try:
            pdf.image("shirtificate.png", 0, 50,keep_aspect_ratio=True)
        except FileNotFoundError:
            sys.exit("No file found")
        pdf.cell(0, 40, "CS50 Shirtificate", align='C')
        pdf.set_font("helvetica", style="B", size=30)
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 240, f"{name} took CS50", align=Align.C, center=True)
        pdf.output("shirtificate.pdf")


def main():
    name = input("Input your name: ")
    pdf = PDF(name)

if __name__ == "__main__":
    main()
