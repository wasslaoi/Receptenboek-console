# Startcode/pdf_export.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

def export_recept_pdf(recept, aantal_personen: int, plantaardig: bool, pad: str) -> str:
    """
    Maakt één PDF-pagina met:
    - Receptnaam, omschrijving
    - Ingrediënten (bullets), geschaald op aantal_personen en variant (plantaardig/ niet)
    - Stappen (genummerd, incl. tips)
    - Totaal kcal
    Retourneert het pad van het PDF-bestand.
    """
    # Schaal intern op gekozen aantal
    recept.set_aantal_personen(aantal_personen)

    # Setup PDF
    c = canvas.Canvas(pad, pagesize=A4)
    width, height = A4
    x_margin = 2 * cm
    y = height - 2 * cm
    line_height = 14

    def write(text, bold=False):
        nonlocal y
        if y < 2*cm:
            c.showPage()
            y = height - 2 * cm
        if bold:
            c.setFont("Helvetica-Bold", 12)
        else:
            c.setFont("Helvetica", 11)
        c.drawString(x_margin, y, text)
        y -= line_height

    # Titel
    write(recept.get_naam(), bold=True)
    # Omschrijving
    write(recept.get_omschrijving())

    # Ingrediënten
    write("")  # lege regel
    write("Ingrediënten:", bold=True)
    for ing in recept.get_ingredienten(plantaardig=plantaardig):
        write(f"• {ing}")

    # Stappen
    write("")  # lege regel
    write("Bereidingsstappen:", bold=True)
    for i, stap in enumerate(recept.get_stappen(), start=1):
        write(f"{i}. {stap}")

    # Totaal kcal
    totaal = recept.totaal_kcal(plantaardig=plantaardig)
    write("")  # lege regel
    write(f"Totaal kcal: {round(totaal, 1)}", bold=True)

    c.save()
    return pad
