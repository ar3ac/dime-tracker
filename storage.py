import json

FILE_PATH = "expenses.json"


def load_expenses():
    """
    load expenses from json file
    return an empty list if file does not exist or is empty
    raise ValueError if file is corrupted
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


def append_expense(expense):
    """Add an expense to the list of expenses."""
    expenses = load_expenses()
    expenses.append(expense)
    write_expenses(expenses)


def write_expenses(expenses):
    """Write the list of expenses to the JSON file."""
    with open(FILE_PATH, "w") as f:
        json.dump(expenses, f, indent=4)
