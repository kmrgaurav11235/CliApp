import click


@click.command()
def cli():
    """My First CLI Script"""
    click.echo(message="Hello World!")
