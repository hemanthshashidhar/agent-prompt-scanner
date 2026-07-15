import typer

from agent.cli.scan import app as scan_app

app = typer.Typer(
    help="AI Agent Verification Platform",
    no_args_is_help=True,
)

app.add_typer(
    scan_app,
    name="scan",
)

if __name__ == "__main__":
    app()
