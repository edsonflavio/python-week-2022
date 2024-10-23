import typer
from typing import Optional
from beerlog.core import add_beer_to_database
from beerlog.core import get_beers_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Meu gestor de Cerveja")
console = Console()

@main.command("add")
def add(
    name:   str, 
    style:  str,
    flavor: int = typer.Option(...),
    image:  int = typer.Option(...),
    cost:   int = typer.Option(...)
):
    """Add uma nova cerveja no BD"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍻 Adicionada ao banco de dados!!")
    else:
        print("\n{no_entry}")

@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lista as cervejas no BD"""
    beers = get_beers_from_database()
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
