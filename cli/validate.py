
# cli/validate.py

import typer
from pathlib import Path
import toml
import yaml
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Confirm

app = typer.Typer(help="Validate the integrity and consistency of an experiment directory")

REQUIRED_TOML_KEYS = [
    "experiment.name",
    "experiment.created",
    "experiment.version",
    "hardware.use_pupil_core",
    "recording.sampling_rate_hz"
]

REQUIRED_PATHS = [
    "data",
    "log",
    "scripts",
    "config"
]

def load_toml_file(path: Path):
    try:
        return toml.load(path)
    except Exception as e:
        print(f"[red]❌ Could not parse TOML file at {path}: {e}[/red]")
        return None

@app.command("experiment")
def validate_experiment(
    path: Path = typer.Argument(..., help="Path to the experiment directory (inside LABORATORY)")
):
    """
    Validate structure, config and metadata of an experiment folder.
    """
    print(Panel.fit(f"[bold cyan]🔍 Validating experiment at: {path}[/bold cyan]"))

    if not path.exists() or not path.is_dir():
        print(f"[red]❌ Directory not found: {path}[/red]")
        raise typer.Exit(code=1)

    toml_file = path / "experiment.toml"
    if not toml_file.exists():
        print(f"[red]❌ experiment.toml not found in {path}[/red]")
        raise typer.Exit(code=1)

    exp_data = load_toml_file(toml_file)
    if exp_data is None:
        raise typer.Exit(code=1)

    # Flatten keys for checking
    def get_nested(d, keys):
        for k in keys:
            d = d.get(k, {})
        return d if d else None

    table = Table(title="Field Check")
    table.add_column("Field")
    table.add_column("Present")
    table.add_column("Value", overflow="fold")

    for key_path in REQUIRED_TOML_KEYS:
        keys = key_path.split(".")
        val = get_nested(exp_data, keys)
        ok = "[green]✔[/green]" if val is not None else "[red]✘[/red]"
        val_str = str(val) if val else "[dim]None[/dim]"
        table.add_row(key_path, ok, val_str)

    print(table)

    # Check folder structure
    print("[bold]📁 Directory Check:[/bold]")
    for folder in REQUIRED_PATHS:
        dir_path = path / folder
        if dir_path.exists() and dir_path.is_dir():
            print(f"[green]✔[/green] {folder}/")
        else:
            print(f"[red]✘[/red] {folder}/ missing")

    print("[bold green]✓ Validation complete.[/bold green]")
