# cli/export.py

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
import shutil
import zipfile
import yaml
from datetime import datetime

app = typer.Typer(help="Export experiments to EXPORTS/ as compressed ZIP archives")

LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"
EXPORTS_ROOT = Path(__file__).parent.parent / "EXPORTS"
EXPORTS_INDEX = EXPORTS_ROOT / "index.yml"
EXPORTS_ROOT.mkdir(parents=True, exist_ok=True)

def load_index(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or []
    return []

def save_index(path, index):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(index, f, sort_keys=False)

def find_experiment(name: str):
    src_lab = LAB_PATH / name
    src_archive = ARCHIVE_PATH / name
    if src_lab.exists():
        return src_lab, "LABORATORY"
    elif src_archive.exists():
        return src_archive, "ARCHIVE"
    else:
        return None, None

def list_existing_exports(exp_name: str) -> list:
    exp_dir = EXPORTS_ROOT / exp_name
    if not exp_dir.exists():
        return []
    return sorted([f.name for f in exp_dir.glob(f"{exp_name}_*.zip")])

def export_zip(experiment_name: str, force: bool):
    src, location = find_experiment(experiment_name)
    if not src:
        typer.secho(f"❌ Experiment '{experiment_name}' not found in LABORATORY or ARCHIVE", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    exp_export_dir = EXPORTS_ROOT / experiment_name
    exp_export_dir.mkdir(parents=True, exist_ok=True)

    # List existing
    existing = list_existing_exports(experiment_name)
    if existing and not force:
        typer.echo("📂 Existing exports:")
        for f in existing:
            typer.echo(f" - {f}")
        if not typer.confirm("Create another export with new timestamp?"):
            typer.secho("❌ Export cancelled.", fg=typer.colors.RED)
            raise typer.Exit()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    zip_name = f"{experiment_name}_{timestamp}.zip"
    zip_path = exp_export_dir / zip_name

    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in src.rglob("*"):
                zipf.write(file, file.relative_to(src.parent))
        typer.secho(f"✅ Exported from {location} to: {zip_path}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to create ZIP: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=2)

    index = load_index(EXPORTS_INDEX)
    entry = {
        "name": experiment_name,
        "path": str(zip_path.relative_to(EXPORTS_ROOT)),
        "timestamp": timestamp,
        "source": location
    }
    index.append(entry)
    save_index(EXPORTS_INDEX, index)
    typer.secho(f"📝 Updated EXPORTS/index.yml", fg=typer.colors.BLUE)

@app.command("experiment")
def export_experiment(
    name: str = typer.Argument(..., help="Name of the experiment to export"),
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation if previous exports exist")
):
    """
    Compress an experiment into a timestamped ZIP archive, whether it's in LABORATORY or ARCHIVE.
    """
    export_zip(name, force)
