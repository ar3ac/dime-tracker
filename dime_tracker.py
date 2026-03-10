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
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
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

    def delete_expense(self, expense_id):
        # Trova la spesa da eliminare
        expense_to_delete = next(
            (e for e in self.expenses if e["id"] == expense_id), None
        )

        # Se non viene trovata, solleva un errore
        if expense_to_delete is None:
            raise ValueError(f"Expense with ID {expense_id} not found.")

        # Ricrea la lista escludendo la spesa da eliminare
        self.expenses = [e for e in self.expenses if e["id"] != expense_id]
        write_expenses(self.expenses)

        return expense_to_delete

    def update_expense(self, expense_id, description=None, amount=None):
        # Trova la spesa da aggiornare
        expense_to_update = next(
            (e for e in self.expenses if e["id"] == expense_id), None
        )

        # Se non viene trovata, solleva un errore
        if expense_to_update is None:
            raise ValueError(f"Expense with ID {expense_id} not found.")

        if amount is not None and amount < 0:
            raise ValueError("Amount cannot be negative.")
        # Aggiorna i campi se sono stati forniti
        if description is not None:
            if not description.strip():
                raise ValueError("Description cannot be empty or contain only spaces.")
            expense_to_update["description"] = description
        if amount is not None:
            expense_to_update["amount"] = amount

        write_expenses(self.expenses)

        return expense_to_update

    def summarize(self, month=None):
        expenses_to_summarize = self.expenses
        if month:
            try:
                month_num = int(month)
                if not 1 <= month_num <= 12:
                    raise ValueError("Month must be a number between 1 and 12.")
            except (ValueError, TypeError):
                raise ValueError("Month must be a number between 1 and 12.")

            expenses_to_summarize = [
                e
                for e in self.expenses
                if datetime.strptime(e["date"], "%Y-%m-%d").month == month_num
            ]

        return sum(e["amount"] for e in expenses_to_summarize)
