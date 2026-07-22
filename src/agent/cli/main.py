import typer 
 
from agent.cli.scan import app as scan_app

app = typer.Typer(
    help="AI Agent Verification Platform"
)

app.add_typer(scan_app, name="")


if __name__ == "__main__":
    app()
