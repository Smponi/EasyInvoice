![Logo](./images/logo.png)
# EasyInvoice

EasyInvoice ist ein Python-basiertes Tool, das ein Command-Line-Interface (CLI) bietet, um PDF-Rechnungen zu generieren und auszufüllen. Es ermöglicht das Ausfüllen von PDF-Rechnungsvorlagen mit benutzerdefinierten Werten und kann für einzelne oder mehrere Monate (bis zu einem Jahr) Rechnungen erstellen.

## Features

- Erstellen von einzelnen oder mehreren Rechnungen für einen definierten Zeitraum (bis zu 12 Monate).
- Ausfüllen von PDF-Rechnungsvorlagen mit benutzerdefinierten Werten wie Brutto, MwSt, Netto, etc.
- Einfache und intuitive Textbenutzeroberfläche.

## Voraussetzungen

Bevor Sie den InvoicePDFGenerator verwenden, stellen Sie sicher, dass Sie Python auf Ihrem System installiert haben. Das Programm wurde mit Python 3.x entwickelt.

## Installation

Um mit dem InvoicePDFGenerator zu starten, klonen Sie das Repository und installieren Sie die erforderlichen Abhängigkeiten:

```bash
git clone https://github.com/Smponi/InvoicePdfGenerator.git
cd InvoicePDFGenerator
pip install -r requirements.txt
```

## Benutzung

Starten Sie das Programm mit dem folgenden Befehl:

```bash
python invoice_generator.py
```

```bash
# Um noch weitere Informationen zu bekommen, einfach das help flag setzen
python invoice_generator.py --help
```

Folgen Sie den Anweisungen in der TUI, um die Rechnungsdaten einzugeben. Nach Abschluss werden die PDF-Rechnungen im angegebenen Verzeichnis generiert.

## Disclaimer
Sollten falsche Einnahmenbelege durch das Programm erstellt werden, die zu Verlusten oder sonstigem führen, übernehmne ich keine Haftung!
Die Ursprungs PDF gehört nicht mir. Sie ist hier zu finden: https://www.amtsvorducke.de/forms/1ea2f4980e82b86b7d4eb3c129225c4b.pdf
Ich habe keinerlei Rechte an der PDF.
Das Logo wurde mit ChatGPT erstellt. 

## Support

Bei Fragen oder Problemen öffnen Sie bitte ein Issue im Repository 
