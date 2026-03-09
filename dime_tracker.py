from storage import load_expenses, append_expense, write_expenses
from datetime import datetime


class DimeTracker:
    def __init__(self):
        self.expenses = load_expenses()

    def add_expense(self, description, amount):
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
        append_expense(expense)
        return expense

    def list_expenses(self):
        return self.expenses
