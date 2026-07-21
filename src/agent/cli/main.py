import typer

from agent.cli.scan import app as scan_app

app = typer.Typer()

app.add_typer(scan_app, name="")


if __name__ == "__main__":
    app()
