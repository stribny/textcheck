from pathlib import Path
from typing import Optional
import typer
from rich.console import Console
from rich.table import Table
from textcheck.lib.spellcheck import check


app = typer.Typer()


@app.command()
def spellcheck(
    files: list[str],
    ignore_list: str = typer.Option(None, help="File with ignore words on new lines"),
):
    """
    Run spellcheck for a set of files
    """
    ignore_words = []
    if ignore_list:
        with open(Path(ignore_list), "r") as f:
            ignore_words = f.read().split("\n")
    console = Console()
    for file in files:
        console.print(f"{file}:")
        with open(Path(file), "r") as f:
            text = f.read()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Word", style="yellow")
        table.add_column("Alternatives")
        table.add_column("Context")
        spell_mistakes = check(text, ignore_words)
        for misspelled in spell_mistakes:
            table.add_row(
                misspelled.word, ", ".join(misspelled.suggestions), misspelled.context
            )
        console.print(table)


@app.callback()
def callback():
    pass
