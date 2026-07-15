import typer

from agent.cli.scan import scan

app = typer.Typer(
    help="AI Agent Verification Platform",
    no_args_is_help=True,
)

app.command("scan")(scan)

if __name__ == "__main__":
    app()
