from rich.console import Console
from rich.table import Table


def display_expenses_table(expenses):
    """Displays a list of expenses in a formatted table using rich."""
    console = Console()

    if not expenses:
        console.print("[yellow]No expenses to show.[/yellow]")
        return
    if len(expenses) == 1:
        title = "Expense added Successfully"
    else:
        title = "Expenses List"
    table = Table(show_header=True, header_style="bold blue", title=title)
    table.add_column("ID", style="dim", width=4, justify="right")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Description", no_wrap=False)
    table.add_column("Amount", justify="right", width=16)

    for expense in expenses:
        color = "bright_green"
        table.add_row(
            str(expense["id"]),
            expense["date"],
            expense["description"],
            f"[{color}]{expense['amount']:.2f}€[/{color}]",
        )

    console.print(table)


def display_error(message):
    """Displays an error message using rich."""
    console = Console()
    console.print(f"[bold red]Error:[/bold red] {message}")


def display_success(message):
    """Displays a success message using rich."""
    console = Console()
    console.print(f"[bold green]Success:[/bold green] {message}")
