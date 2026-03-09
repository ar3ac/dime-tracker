from storage import load_expenses, write_expenses
from datetime import datetime


class DimeTracker:
    def __init__(self):
        self.expenses = load_expenses()

    def add_expense(self, description, amount):
        # Argparse already ensures amount is a float.
        # We just need to validate that the description is not empty or just whitespace.
        if not description.strip():
            raise ValueError("Description cannot be empty or contain only spaces.")

        if self.expenses:
            new_id = max(e["id"] for e in self.expenses) + 1
        else:
            new_id = 1
        expense = {
            "id": new_id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "description": description,
            "amount": amount,
        }
        self.expenses.append(expense)
        write_expenses(self.expenses)
        return expense

    def list_expenses(self):
        return self.expenses
