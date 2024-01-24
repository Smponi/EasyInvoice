import os
import typer
import json
from invoice_logic import generate_invoice
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

app = typer.Typer()
console = Console()

def ensure_output_directory():
    """Stellt sicher, dass der Ausgabeordner existiert, und erstellt ihn, falls nötig."""
    output_dir = "./output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def save_config(invoice_data):
    """Speichert die eingegebenen Daten als Konfigurationsdatei."""
    if typer.confirm("Möchten Sie die Daten als Konfigurationsdatei speichern?",True):
        config_name = typer.prompt("Geben Sie den Namen der Konfigurationsdatei ein")
        with open(f"{config_name}.json", 'w') as file:
            json.dump(invoice_data, file, indent=4)
        console.print(f"[green]Konfigurationsdatei '{config_name}.json' gespeichert.[/green]")

def load_config(config_path: str):
    """Lädt Konfigurationsdaten aus einer JSON-Datei."""
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        console.print("[red]Config-Datei nicht gefunden.[/red]")
        raise typer.Exit()

def collect_invoice_data():
    """Sammelt Rechnungsdaten vom Benutzer."""
    data = {}
    data["year"] = Prompt.ask("Jahr")
    data["generate_12"] = typer.confirm("12 Rechnungen für das ganze Jahr erstellen?")
    data["brutto"] = Prompt.ask("Brutto")
    data["mwsatz"] = Prompt.ask("MwSt-Satz")
    data["mwst"] = Prompt.ask("MwSt")
    data["netto"] = Prompt.ask("Netto")
    data["betrag_in_worten"] = Prompt.ask("Betrag in Worten")
    data["zahlung_von"] = Prompt.ask("Zahlung von")
    data["verwendungszweck"] = Prompt.ask("Verwendungszweck")
    data["ort"] = Prompt.ask("Ort")
    data["kontierung"] = Prompt.ask("Kontierung")
    return data

@app.command()
def create_invoice(config: str = typer.Option(None, "--config", "-c", help="Pfad zur Konfigurationsdatei")):
    """Erstellt Rechnungen basierend auf einer Konfigurationsdatei oder Benutzereingaben."""
    if config:
        invoice_data = load_config(config)
    else:
        invoice_data = collect_invoice_data()

    # Zeige eine Übersicht der eingegebenen Daten
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Feld", style="dim")
    table.add_column("Wert")

    for key, value in invoice_data.items():
        table.add_row(key, str(value))

    console.print(table)
    if typer.confirm("Sind diese Informationen korrekt?", default=True):
        output_path = ensure_output_directory()
        generate_invoice("./Einnahmbeleg.pdf", output_path, invoice_data)
        save_config(invoice_data)
    else:
        typer.echo("Abbruch der Rechnungserstellung.")



if __name__ == "__main__":
    app()
