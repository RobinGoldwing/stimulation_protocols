# cli/doctor.py

import typer
import platform
import sys
import os
import importlib.util
from rich import print
from rich.panel import Panel
from rich.table import Table

app = typer.Typer(help="Diagnose the current XTIM environment and dependencies")

REQUIRED_MODULES = [
    "typer", "cookiecutter", "pylsl", "psychopy", "pandas", "numpy", "rich"
]

def check_module(name):
    spec = importlib.util.find_spec(name)
    return spec is not None

@app.command("status")
def status():
    """Show system and environment diagnostics"""
    print(Panel.fit("[bold cyan]XTIM Environment Diagnostic[/bold cyan]"))

    # Python info
    print(f"[bold]Python executable:[/bold] {sys.executable}")
    print(f"[bold]Python version:[/bold] {platform.python_version()}")
    print(f"[bold]Platform:[/bold] {platform.system()} {platform.release()}")

    # Conda environment
    conda_env = os.environ.get("CONDA_DEFAULT_ENV", "Not detected")
    print(f"[bold]Conda environment:[/bold] {conda_env}")

    # PYTHONPATH
    py_path = os.environ.get("PYTHONPATH", None)
    print(f"[bold]PYTHONPATH:[/bold] {py_path or '[dim]Not set[/dim]'}")

    # Module checks
    table = Table(title="Required Python Modules")
    table.add_column("Module", style="cyan")
    table.add_column("Available", justify="center")

    for module in REQUIRED_MODULES:
        status = "[green]✔[/green]" if check_module(module) else "[red]✘[/red]"
        table.add_row(module, status)

    print(table)

    print("[bold green]✓ Done.[/bold green] If any modules are missing, install with:")
    print("  [yellow]pip install -r config/requirements.txt[/yellow] or update your Conda environment.\n")

