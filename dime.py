from dime_tracker import DimeTracker
import argparse
from datetime import datetime
from view import display_expenses_table, display_error


def main():
    parser = argparse.ArgumentParser(description="Dime - A simple expense tracker")
    # inizialize subparsers for "add" and "list" commands
    subparsers = parser.add_subparsers(
        dest="command", help="Available commands", required=True
    )

    # configure for "add" command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument(
        "--description", help="Description of the expense", required=True
    )
    add_parser.add_argument(
        "--amount", type=float, help="Amount of the expense", required=True
    )

    # configure for "list" command
    list_parser = subparsers.add_parser("list", help="List all expenses")

    args = parser.parse_args()

    try:
        dime = DimeTracker()
        if args.command == "add":
            expense = dime.add_expense(description=args.description, amount=args.amount)
            display_expenses_table([expense])
        elif args.command == "list":
            expenses = dime.list_expenses()
            display_expenses_table(expenses)
    except ValueError as e:
        display_error(str(e))


if __name__ == "__main__":
    main()
