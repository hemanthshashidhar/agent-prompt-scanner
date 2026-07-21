from pathlib import Path

import typer
from rich import print

from agent.core.project_loader import ProjectLoader
from agent.report.renderer import ReportRenderer
from agent.scanner.prompt import PromptScanner

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
    result = scanner.scan(project_path)

    renderer = ReportRenderer()
    renderer.render(result)
