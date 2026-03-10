from dime_tracker import DimeTracker
import argparse
from datetime import datetime
from view import display_expenses_table, display_error, display_success


def main():
    parser = argparse.ArgumentParser(description="Dime - A simple expense tracker")
    # Inizializza i subparser per i comandi
    subparsers = parser.add_subparsers(
        dest="command", help="Available commands", required=True
    )

    # Configura il comando "add"
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument(
        "--description", help="Description of the expense", required=True
    )
    add_parser.add_argument(
        "--amount", type=float, help="Amount of the expense", required=True
    )

    # Configura il comando "list"
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Configura il comando "delete"
    delete_parser = subparsers.add_parser("delete", help="Delete an expense by ID")
    delete_parser.add_argument(
        "--id", type=int, help="ID of the expense to delete", required=True
    )

    # Configura il comando "update" con argomenti opzionali per descrizione e importo
    update_parser = subparsers.add_parser("update", help="Update an expense by ID")
    update_parser.add_argument(
        "--id", type=int, help="ID of the expense to update", required=True
    )
    update_parser.add_argument("--description", help="New description of the expense")
    update_parser.add_argument("--amount", type=float, help="New amount of the expense")

    # Configura il comando "summary"
    summary_parser = subparsers.add_parser(
        "summary", help="Show a summary of expenses by month"
    )
    summary_parser.add_argument(
        "--month",
        type=str,
        help="Month to summarize (number of the month)",
        required=False,
    )

    args = parser.parse_args()

    try:
        dime = DimeTracker()
        if args.command == "add":
            expense = dime.add_expense(description=args.description, amount=args.amount)
            display_expenses_table([expense])
        elif args.command == "list":
            expenses = dime.list_expenses()
            if not expenses:
                display_error("No expenses to show.")
            else:
                display_expenses_table(expenses)
        elif args.command == "delete":
            deleted_expense = dime.delete_expense(expense_id=args.id)
            display_success(
                f"Expense '{deleted_expense['description']}' (ID: {args.id}) deleted successfully."
            )
        elif args.command == "update":
            if args.description is None and args.amount is None:
                display_error(
                    "Please provide at least a new description (--description) or a new amount (--amount) to update."
                )
                return

            updated_expense = dime.update_expense(
                expense_id=args.id, description=args.description, amount=args.amount
            )
            display_success(
                f"Expense '{updated_expense['description']}' (ID: {args.id}) updated successfully."
            )
        elif args.command == "summary":
            total = dime.summarize(month=args.month)
            month_name = (
                datetime.strptime(args.month, "%m").strftime("%B") if args.month else ""
            )
            message = (
                f"Total expenses for {month_name}: {total:.2f}€"
                if args.month
                else f"Total expenses: {total:.2f}€"
            )
            display_success(message)

    except ValueError as e:
        display_error(str(e))


if __name__ == "__main__":
    main()
