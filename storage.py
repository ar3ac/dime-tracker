import json
import os

file_path = "expenses.json"


def check_expenses_file():
    if not os.path.exists("expenses.json"):
        with open("expenses.json", "w") as f:
            json.dump([], f)
            f.close()


def load_expenses():
    check_expenses_file()
    try:
        with open("expenses.json", "r") as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("The expenses.json file is corrupted and cannot be read.")


def write_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)
