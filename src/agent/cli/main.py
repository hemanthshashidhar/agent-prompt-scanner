import typer

from agent.cli.scan import scan

app = typer.Typer(
    help="AI Agent Verification Platform",
    no_args_is_help=True,
)


@app.callback()
def main():
    """Agent CLI."""
    pass


app.command(name="scan")(scan)

if __name__ == "__main__":
    app()
