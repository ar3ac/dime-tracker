from DimeTracker import DimeTracker
import argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Dime - A simple expense tracker")
    # inizialize subparsers for "add" and "list" commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # configure for "add" command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", help="Description of the expense")
    add_parser.add_argument("--amount", type=float, help="Amount of the expense")

    # configure for "list" command
    list_parser = subparsers.add_parser("list", help="List all expenses")

    args = parser.parse_args()

    dime = DimeTracker()

    if args.command == "add":
        expense = dime.add_expense(description=args.description, amount=args.amount)
        print(f"Expense added successfully with ID {expense['id']}: {expense}")
    elif args.command == "list":
        expenses = dime.list_expenses()
        print(expenses)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
