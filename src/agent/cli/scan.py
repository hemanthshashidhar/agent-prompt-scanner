from pathlib import Path

import typer
from rich.console import Console

from agent.scanner.prompt import PromptScanner

app = typer.Typer()

console = Console()


@app.callback(invoke_without_command=True)
def scan(
    path: Path = typer.Argument(
        Path("."),
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
):

    scanner = PromptScanner()

    result = scanner.scan(path)

    console.rule("[bold cyan]Agent Verify[/bold cyan]")

    console.print(f"Scanner : {scanner.name}")
    console.print(f"Project : {path}")
    console.print(f"Findings: {len(result.findings)}")
