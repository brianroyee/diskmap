from diskmap.scanner import scan_directory
from diskmap.largest import find_largest_files
from diskmap.visualizer import display_folders
from rich.console import Console

console = Console()


def run(path):

    console.print(f"\nScanning [bold green]{path}[/bold green]\n")

    folders = scan_directory(path)

    display_folders(folders)

    console.print("\n[bold yellow]Largest Files[/bold yellow]\n")

    largest = find_largest_files(path)

    for file, size in largest:

        console.print(f"{file} ({size/1024/1024:.2f} MB)")