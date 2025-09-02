import typer

app = typer.Typer()


@app.command()
def hello():
    """No-op command for Session 1."""
    typer.echo("hello from rlvr")


if __name__ == "__main__":
    app()
