from pathlib import Path

import typer
from rich.console import Console

from agent.scanner.prompt import PromptScanner

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
    scanner = PromptScanner()
    result = scanner.scan(path)

    console.rule("[bold cyan]Agent Verify[/bold cyan]")
    console.print(f"Scanner : {scanner.name}")
    console.print(f"Project : {path}")
    console.print(f"Findings: {len(result.findings)}")
