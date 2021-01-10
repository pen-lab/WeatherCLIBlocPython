import typer


def weather(
        city: str = typer.Argument(...)
):
    typer.echo(f'weather to {city}')


def main():
    typer.run(weather)

