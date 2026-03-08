import json

FILE_PATH = "expenses.json"


def load_expenses():
    """
    Carica le spese dal file JSON.
    Restituisce una lista vuota se il file non esiste o è vuoto.
    Solleva un ValueError se il file è corrotto.
    """
    try:
        with open(FILE_PATH, "r") as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        # Se il file non esiste, è come non avere ancora spese.
        return []
    except json.JSONDecodeError:
        raise ValueError(f"Il file {FILE_PATH} è corrotto e non può essere letto.")


def write_expenses(expenses):
    """Scrive la lista di spese nel file JSON."""
    with open(FILE_PATH, "w") as f:
        json.dump(expenses, f, indent=4)
