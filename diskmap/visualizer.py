from rich.console import Console
from rich.table import Table

console = Console()


def human_size(size):

    for unit in ["B", "KB", "MB", "GB", "TB"]:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024


def display_folders(data):

    table = Table(title="DiskMap Folder Usage")

    table.add_column("Folder", style="cyan")
    table.add_column("Size", style="magenta")

    for folder, size in data:

        table.add_row(folder, human_size(size))

    console.print(table)