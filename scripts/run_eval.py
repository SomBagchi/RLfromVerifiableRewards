import typer

app = typer.Typer()


@app.command()
def main():
    """Help-only CLI in Session 1."""
    typer.echo("stub")


if __name__ == "__main__":
    app()
