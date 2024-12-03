from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

console = Console()

def mixed_up_calculator():
    while True:
        console.print(Panel(Text("✨ Welcome to the Mixed-Up Calculator! ✨", style="bold cyan"), expand=False))

        num1 = float(Prompt.ask("Enter the first number", console=console))
        num2 = float(Prompt.ask("Enter the second number", console=console))

        operation = Prompt.ask("Choose an operation (+, -, *, /)", choices=["+", "-", "*", "/"], console=console)

        if operation == "+":
            user_result = num1 + num2
            actual_operation = "*"
            actual_result = num1 * num2
        elif operation == "-":
            user_result = num1 - num2
            actual_operation = "/"
            actual_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
        elif operation == "*":
            user_result = num1 * num2
            actual_operation = "+"
            actual_result = num1 + num2
        elif operation == "/":
            user_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
            actual_operation = "-"
            actual_result = num1 - num2

        console.print(
            Panel(
                f"[bold yellow]Your choice:[/bold yellow] [cyan]{operation}[/cyan]\n"
                f"[bold blue]Result of your operation:[/bold blue] [green]{user_result}[/green]\n\n"
                f"[bold green]Actual operation performed:[/bold green] [red]{actual_operation}[/red]\n"
                f"[bold magenta]Result of actual operation:[/bold magenta] [white]{actual_result}[/white]",
                title="Mixed-Up Calculator Results",
                border_style="bright_blue",
            )
        )

        continue_choice = Prompt.ask(
            "Do you want to perform another calculation? (yes/no)", choices=["yes", "no"], console=console
        )
        if continue_choice == "no":
            console.print(
                Panel(
                    Text("💡 Thank you for using the Mixed-Up Calculator! Goodbye! 💡", style="bold green"),
                    expand=False,
                )
            )
            break

mixed_up_calculator()
