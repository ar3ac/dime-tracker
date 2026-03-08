from storage import load_expenses, write_expenses

expense = {
    "id": "1",
    "date": "2024-06-01",
    "description": "Groceries",
    "amount": 50.0,
}

write_expenses([expense])

expenses = load_expenses()
print(expenses)
