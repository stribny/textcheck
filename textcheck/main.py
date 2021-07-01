from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table
from textcheck.lib.spellcheck import check


app = typer.Typer()


@app.command()
def spellcheck(files: list[str]):
    """
    Run spellcheck for a set of files
    """
    ignore_words = []
    console = Console()
    for file in files:
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
