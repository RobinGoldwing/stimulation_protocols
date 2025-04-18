# cli/config.py

# =============================================================================
# XTIM – Experimental Toolkit for Multimodal Neuroscience
# =============================================================================
# Part of the XSCAPE Project (Experimental Science for Cognitive and Perceptual Exploration)
#
# Developed by:
#   - Arturo-José Valiño
#   - Rubén Álvarez-Mosquera
#
# This software is designed to facilitate the creation, execution, and analysis
# of neuroscience experiments involving eye-tracking, EEG, and other modalities.
# It integrates with hardware and software tools such as Pupil Labs, Emobit,
# and MilliKey MH5, providing a unified command-line interface and interactive
# menu system for experiment management.
#
# For more information about the XSCAPE project, please refer to the project's
# documentation or contact the developers.
# =============================================================================

import typer
import yaml
from pathlib import Path
from rich import print
from rich.table import Table
from rich.panel import Panel
import toml

app = typer.Typer(help="View or modify global XTIM configuration")

DEFAULT_CONFIG = Path(__file__).parent.parent / "config" / "xtim-config.yml"
LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"

def load_config(path: Path):
    if not path.exists():
        print(f"[yellow]⚠ Config file not found at {path}[/yellow]")
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def save_config(path: Path, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)
    print(f"[green]✅ Config saved to {path}[/green]")

@app.command("show")
def show_config(config: Path = typer.Option(DEFAULT_CONFIG, "--config", "-c", help="Path to config file")):
    """
    Show the current global configuration.
    """
    data = load_config(config)
    if not data:
        print("[red]❌ No configuration found.[/red]")
        return
    table = Table(title=f"XTIM Config: {config}")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="white")
    for k, v in data.items():
        table.add_row(k, str(v))
    print(table)

@app.command("get")
def get_value(
    key: str = typer.Argument(..., help="Key to retrieve"),
    config: Path = typer.Option(DEFAULT_CONFIG, "--config", "-c", help="Path to config file")
):
    """
    Get a specific config value by key.
    """
    data = load_config(config)
    value = data.get(key)
    if value is not None:
        print(f"[bold]{key}[/bold] = {value}")
    else:
        print(f"[yellow]⚠ Key '{key}' not found in config.[/yellow]")

@app.command("set")
def set_value(
    key: str = typer.Argument(..., help="Key to set"),
    value: str = typer.Argument(..., help="Value to assign"),
    config: Path = typer.Option(DEFAULT_CONFIG, "--config", "-c", help="Path to config file")
):
    """
    Set a value in the config.
    """
    data = load_config(config)
    data[key] = value
    save_config(config, data)

@app.command("export")
def export_config(
    out: Path = typer.Option(..., help="Destination path for the exported config"),
    config: Path = typer.Option(DEFAULT_CONFIG, "--config", "-c", help="Path to config file")
):
    """
    Export the current configuration to a different file.
    """
    data = load_config(config)
    if not data:
        print("[red]❌ Nothing to export.[/red]")
        return
    save_config(out, data)

@app.command("show-experiment")
def show_experiment(
    name: str = typer.Argument(..., help="Name of the experiment to show")
):
    """
    Show the content of experiment.toml if found in LABORATORY or ARCHIVE.
    """
    for base in [LAB_PATH, ARCHIVE_PATH]:
        candidate = base / name / "config" / "experiment.toml"
        if candidate.exists():
            try:
                meta = toml.load(candidate)
                panel = Panel.fit(f"[bold cyan]Experiment: {meta['experiment'].get('name', name)}[/bold cyan]", style="green")
                print(panel)

                print(Panel.fit(f"📁 Path: {candidate}", title="📁 Experiment path"))


                table = Table(title="experiment.toml")
                table.add_column("Key", style="cyan")
                table.add_column("Value", style="white")

                for section in ["experiment", "hardware", "recording", "paths", "participant", "tags"]:
                    data = meta.get(section, {})
                    for k, v in data.items():
                        table.add_row(f"{section}.{k}", str(v))

                print(table)
                return
            except Exception as e:
                print(f"[red]❌ Failed to parse {candidate}: {e}[/red]")
                return

    print(f"[red]❌ Experiment '{name}' not found in LABORATORY or ARCHIVE[/red]")
