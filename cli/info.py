# cli/info.py

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
from pathlib import Path
import toml
import yaml
from rich import print
from rich.panel import Panel
from rich.table import Table

app = typer.Typer(help="Display metadata and summary information about a given experiment")

LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"
EXPORTS_PATH = Path(__file__).parent.parent / "EXPORTS"

def load_toml(path: Path):
    try:
        return toml.load(path)
    except Exception as e:
        print(f"[red]❌ Failed to load TOML file: {e}[/red]")
        return None

def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[red]❌ Failed to load YAML file: {e}[/red]")
        return None

def print_dict_section(title, data):
    t = Table(title=title)
    t.add_column("Key", style="yellow")
    t.add_column("Value", style="white")
    for k, v in data.items():
        t.add_row(k, str(v))
    print(t)

@app.command("experiment")
def info_experiment(
    name: str = typer.Argument(..., help="Name of the experiment")
):
    """
    Display information from experiment.toml, display-conf.yml, and any ZIPs in EXPORTS/
    """
    found = None
    for base in [LAB_PATH, ARCHIVE_PATH]:
        if (base / name).exists():
            found = base / name
            break

    print(Panel.fit(f"📊 Retrieving info: {name}", title="XTIM Info"))

    if found is None:
        print(f"[red]❌ Experiment '{name}' not found in LABORATORY or ARCHIVE[/red]")
    else:
        toml_path = found / "config" / "experiment.toml"
        yml_path = found / "config" / "display-conf.yml"

        meta = load_toml(toml_path)
        if meta:
            panel = Panel.fit(f"[bold cyan]{meta['experiment'].get('name', name)}[/bold cyan]", title="Experiment")
            print(panel)
            
            print(Panel.fit(f"📁 Experiment path: {found}", title="📁 Experiment path"))

            table = Table(title="Basic Metadata")
            table.add_column("Key", style="green")
            table.add_column("Value", style="white")

            for key in ["description", "author", "email", "version", "created", "uuid"]:
                val = meta["experiment"].get(key, "-")
                table.add_row(key, str(val))

            print(table)

            print_dict_section("Hardware", meta.get("hardware", {}))
            print_dict_section("Recording", meta.get("recording", {}))
            print_dict_section("Paths", meta.get("paths", {}))
            print_dict_section("Participant", meta.get("participant", {}))
            print_dict_section("Tags", meta.get("tags", {}))

        if yml_path.exists():
            yml = load_yaml(yml_path)
            print_dict_section("Monitor", yml.get("monitor", {}))
            print_dict_section("Display", yml.get("display", {}))
            print_dict_section("Sync", yml.get("sync", {}))
        else:
            print("[dim]No display-conf.yml found.[/dim]")

    # Check EXPORTS
    export_dir = EXPORTS_PATH / name
    if export_dir.exists():
        zips = sorted([f.name for f in export_dir.glob("*.zip")])
        if zips:
            print(Panel.fit(f"📂 Export path: {export_dir}", title="📦 Export Path"))
            print(Panel.fit("\n".join(zips), title="📦 Exported ZIPs", style="dim"))
        else:
            print("[yellow]⚠ EXPORTS folder exists but has no ZIPs.[/yellow]")
    else:
        print("[dim]No EXPORTS folder found for this experiment.[/dim]")
