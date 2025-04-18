# cli/validate.py


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

app = typer.Typer(help="Validate experiment folders and related exports.")

LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"
EXPORTS_PATH = Path(__file__).parent.parent / "EXPORTS"

def validate_toml(toml_path: Path):
    required = ["name", "uuid", "created"]
    ok = True

    try:
        meta = toml.load(toml_path)
        exp = meta.get("experiment", {})
        table = Table(title="experiment.toml")
        table.add_column("Field", style="cyan")
        table.add_column("Status", style="green")

        for field in required:
            if field in exp:
                table.add_row(field, "✅")
            else:
                table.add_row(field, "[yellow]⚠ missing[/yellow]")
                ok = False

        print(table)
    except Exception as e:
        print(f"[red]❌ Failed to read {toml_path.name}: {e}[/red]")
        ok = False
    return ok

def validate_display(yml_path: Path):
    required = ["resolution", "refresh_rate_hz"]
    ok = True

    try:
        disp = yaml.safe_load(yml_path.read_text(encoding="utf-8"))
        mon = disp.get("monitor", {})
        table = Table(title="display-conf.yml")
        table.add_column("Field", style="cyan")
        table.add_column("Status", style="green")

        for field in required:
            if field in mon:
                table.add_row(field, "✅")
            else:
                table.add_row(field, "[yellow]⚠ missing[/yellow]")
                ok = False

        print(table)
    except Exception as e:
        print(f"[red]❌ Failed to read {yml_path.name}: {e}[/red]")
        ok = False
    return ok

def list_exports(name: str):
    exports = EXPORTS_PATH / name
    if exports.exists():
        files = sorted(f.name for f in exports.glob("*.zip"))
        if files:
            print(Panel.fit("\n".join(files), title="📦 Exported ZIPs in EXPORTS/", style="dim"))
        else:
            print("[yellow]⚠ No ZIPs found in EXPORTS/[/yellow]")
    else:
        print("[dim]No export folder found for this experiment.[/dim]")

@app.command("experiment")
def validate_experiment(
    name: str = typer.Argument(..., help="Name of the experiment (without full path)")
):
    """
    Validate an experiment by name, searching LABORATORY/ and ARCHIVE/, and show any exports in EXPORTS/
    """
    base_path = None
    for folder in [LAB_PATH, ARCHIVE_PATH]:
        candidate = folder / name
        if candidate.exists():
            base_path = candidate
            break

    print(Panel.fit(f"🧪 Validating experiment: {name}", title="XTIM Validate"))

    if base_path is None:
        print(f"[red]❌ Experiment '{name}' not found in LABORATORY/ or ARCHIVE/[/red]")
        raise typer.Exit()

    config_path = base_path / "config"
    toml_path = config_path / "experiment.toml"
    yml_path = config_path / "display-conf.yml"

    toml_ok = validate_toml(toml_path)
    yml_ok = validate_display(yml_path)

    list_exports(name)

    if toml_ok and yml_ok:
        print(f"[green]✅ Experiment '{name}' is valid.[/green]")
    else:
        print(f"[yellow]⚠ Some issues found in experiment '{name}'.[/yellow]")
