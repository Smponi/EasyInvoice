import json

def read_config(file_path):
    """Liest die Konfigurationsdaten aus einer JSON-Datei."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def write_config(file_path, config_data):
    """Schreibt die Konfigurationsdaten in eine JSON-Datei."""
    with open(file_path, 'w') as file:
        json.dump(config_data, file, indent=4)
