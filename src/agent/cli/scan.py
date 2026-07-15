from pathlib import Path

import typer
from rich.console import Console

console = Console()


def scan(
    path: Path = typer.Argument(
        Path("."),
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
        help="Path to agent project",
    ),
):
    console.rule("[bold cyan]Agent Verify[/bold cyan]")

    console.print(f"[green]Scanning:[/green] {path}")

    console.print()

    console.print("[yellow]No scanners registered.[/yellow]")

    console.print()

    console.print("[bold green]Done[/bold green]")
