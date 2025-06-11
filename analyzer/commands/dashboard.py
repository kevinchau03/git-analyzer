from rich.panel import Panel
from rich.console import Console
from rich.table import Table

def handle_dashboard(args):
    console = Console()

    # Header
    console.print(Panel.fit("[bold green]Git Analyze CLI[/bold green]\n\n[dim]Welcome User, understand your repo like never before.[/dim]"))

    # Commands table
    table = Table(title="📦 Available Commands", show_header=True, header_style="bold magenta")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")

    table.add_row("dashboard", "Show this overview screen")
    table.add_row("summary", "Show total commits, authors, recent messages")
    table.add_row("log", "Export today's commits to a markdown devlog")

    console.print(table)

    # Footer
    console.print("\n✨ [bold]Created By:[/bold] Kevin Chau, kevchau03 (github)\n")
