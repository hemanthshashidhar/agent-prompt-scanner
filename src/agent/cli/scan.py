from pathlib import Path

import typer
from rich import print

from agent.core.project_loader import ProjectLoader
from agent.scanner.prompt import PromptScanner
from agent.report.renderer import ReportRenderer

app = typer.Typer()


@app.command()
def scan(path: str = typer.Argument(..., help="Path to project")):
    """Scan a project for prompt security issues."""

    loader = ProjectLoader(path)

    if not loader.exists():
        print(f"[red]Error:[/red] Project '{path}' does not exist.")
        raise typer.Exit(code=1)

    project_path: Path = loader.root()

    scanner = PromptScanner()
    renderer = ReportRenderer()
    renderer.render(result)

    print()
    print("[bold cyan]Agent Verify[/bold cyan]")
    print("[bold]==============================[/bold]")

    if not result.findings:
        print("[green]✓ No findings found.[/green]")
        return

    print(f"[bold red]Findings ({len(result.findings)})[/bold red]")
    print()

    for finding in result.findings:
        print(f"[bold]{finding.id}[/bold] [{finding.severity.value}]")
        print(f"Title          : {finding.title}")
        print(f"File           : {finding.file}")
        print(f"Description    : {finding.description}")
        print(f"Recommendation : {finding.recommendation}")
        print()
