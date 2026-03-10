# Dime — CLI Expense Tracker

Your new best friend for realizing you're broke. In real-time.

A simple command-line application to manage your personal expenses. All data is saved locally in an `expenses.json` file.
(a roadmap.sh project : https://roadmap.sh/projects/expense-tracker)

## Features

- ✅ Add, list, update, and delete expenses.
- ✅ Get a summary of total expenses, with an option to filter by month.
- ✅ Clean and readable tabular display for expenses.
- ✅ Intuitive command-line interface.
- ✅ Persistent data storage in a simple JSON file.
- ✅ Input validation and clear error messages.

## Installation

Make sure you have Python 3.8+ installed. Clone the repository and run:

```bash
pip install -r requirements.txt
```

## Use

### Add a new expense

```bash
python dime.py add --description "Lunch" --amount 12.50
```

**Output:**

```
ID  Date       Description  Amount
1   2026-03-10 Lunch        €12.50
```

### Display all expenses

```bash
python dime.py list
```

**Output:**

```
ID  Date       Description         Amount
1   2026-03-08 Coffee             €5.00
2   2026-03-09 Dinner             €25.00
3   2026-03-10 Lunch              €12.50
```

### Delete an expense

```bash
python dime.py delete --id 2
```

**Output:**

```
Success: Expense 'Dinner' (ID: 2) deleted successfully.
```

### Update an expense

update only the description:

```bash
python dime.py update --id 1 --description "Coffee and pastry"
```

or the amount:

```bash
python dime.py update --id 1 --amount 6.50
```

or both:

```bash
python dime.py update --id 1 --description "Coffee and pastry" --amount 6.50
```

### Display summary

Total expenses:

```bash
python dime.py summary
```

**Output:**

```
Success: Total expenses: 42.50€
```

By specific month (1-12):

```bash
python dime.py summary --month 3
```

**Output:**

```
Success: Total expenses for March: 42.50€
```

## Data Structure

Each expense is stored in `expenses.json` with the following format:

```json
{
  "id": 1,
  "date": "2026-03-10",
  "description": "Lunch",
  "amount": 12.5
}
```

## Error Handling

- The application validates input and returns clear error messages:
- Negative or zero amounts are not allowed
- Description cannot be empty
- Month must be a number between 1 and 12
- IDs must exist in the database

Example:

```bash
python dime.py add --description "Test" --amount -5
```

**Output:**

```
Error: Amount cannot be negative.
Error: Amount cannot be negative.
```
