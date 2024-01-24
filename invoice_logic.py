import pdfrw
from datetime import datetime

def fill_pdf_field(pdf, annot_index, value):
    pdf.Root.Pages.Kids[0].Annots[annot_index].update(pdfrw.PdfDict(V=value))
    pdf.Root.Pages.Kids[0].Annots[annot_index + 10].update(pdfrw.PdfDict(V=value))


def generate_invoice(pdf_template_path, output_path, invoice_data):
    """Generiert Rechnungen basierend auf den gegebenen Daten."""
    months = range(1, 13) if invoice_data['generate_12'] else [datetime.now().month]
    year = invoice_data['year']
    german_months = ["Januar", "Februar", "März", "April", "Mai", "Juni",
                     "Juli", "August", "September", "Oktober", "November", "Dezember"]

    for month in months:
        filled_pdf = pdfrw.PdfReader(pdf_template_path)  # Reload template for each month
        date_str = f"01.{month:02d}.{year}"
        month_str = german_months[month - 1]
        verwendungszweck = f"{invoice_data['verwendungszweck']} {month_str[:3]} {year}"
        ort_datum = f"{invoice_data['ort']}, den {date_str}"

        # Fülle die PDF-Felder
        fill_pdf_field(filled_pdf, 0, "")  # BelegNummer (leer)
        fill_pdf_field(filled_pdf, 1, invoice_data['brutto'])      # Brutto
        fill_pdf_field(filled_pdf, 2, invoice_data['mwsatz'])      # MwSt-Satz
        fill_pdf_field(filled_pdf, 3, invoice_data['mwst'])        # MwSt
        fill_pdf_field(filled_pdf, 4, invoice_data['netto'])       # Netto
        fill_pdf_field(filled_pdf, 5, invoice_data['betrag_in_worten'])  # Betrag in Worten
        fill_pdf_field(filled_pdf, 6, invoice_data['zahlung_von'])  # Zahlung von
        fill_pdf_field(filled_pdf, 7, verwendungszweck)  # Verwendungszweck
        fill_pdf_field(filled_pdf, 8, ort_datum)  # Ort und Datum
        fill_pdf_field(filled_pdf, 9, invoice_data['kontierung'])   # Kontierung

        output_filename = f"{output_path}/Rechnung_{month_str}_{invoice_data['year']}.pdf"
        pdfrw.PdfWriter().write(output_filename, filled_pdf)
        print(f"Rechnung für {month_str} {invoice_data['year']} wurde erstellt: {output_filename}")
