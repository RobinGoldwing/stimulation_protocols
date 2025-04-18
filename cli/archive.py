# cli/archive.py

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
import yaml
import shutil
from datetime import datetime
import toml

app = typer.Typer(help="Archive experiments to the ARCHIVE folder")

LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"
LAB_INDEX = LAB_PATH / "index.yml"
ARCHIVE_INDEX = ARCHIVE_PATH / "index.yml"

def load_index(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or []
    return []

def save_index(path, index):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(index, f, sort_keys=False)

def extract_metadata(exp_dir: Path):
    meta = {
        "name": exp_dir.name,
        "archived_at": datetime.now().isoformat(timespec="seconds"),
        "from": "LABORATORY"
    }
    toml_path = exp_dir / "config" / "experiment.toml"
    if toml_path.exists():
        try:
            t = toml.load(toml_path)
            exp = t.get("experiment", {})
            meta["uuid"] = exp.get("uuid")
            meta["created"] = exp.get("created")
            meta["author"] = exp.get("author")
            meta["description"] = exp.get("description")
        except Exception:
            pass
    return meta

@app.command("experiment")
def archive_experiment(
    name: str = typer.Argument(..., help="Name of the experiment to archive"),
    force: bool = typer.Option(False, "--force", "-f", help="Archive without confirmation"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview the archive operation without changing anything"),
):
    """
    Move an experiment from LABORATORY/ to ARCHIVE/ and update both index.yml files accordingly.
    """
    source_path = LAB_PATH / name
    target_path = ARCHIVE_PATH / name

    if not source_path.exists():
        typer.secho(f"❌ Experiment '{name}' not found in LABORATORY/", fg=typer.colors.RED)
        raise typer.Exit()

    if dry_run:
        typer.echo(f"[dry-run] Would move {source_path} → {target_path}")
        return

    if not force:
        confirm = typer.confirm(f"Archive experiment '{name}' to ARCHIVE/?")
        if not confirm:
            typer.secho("❌ Aborted.", fg=typer.colors.RED)
            raise typer.Exit()

    # Ensure ARCHIVE folder exists
    ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)

    # Move the directory
    try:
        shutil.move(str(source_path), str(target_path))
        typer.secho(f"📦 Archived: {name}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to move experiment: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=2)

    # Update LABORATORY index.yml
    index = load_index(LAB_INDEX)
    updated = []
    for entry in index:
        if entry.get("name") == name:
            entry["archived"] = True
        updated.append(entry)
    save_index(LAB_INDEX, updated)
    typer.secho(f"📝 Updated LABORATORY/index.yml", fg=typer.colors.BLUE)

    # Update ARCHIVE index
    archive_index = load_index(ARCHIVE_INDEX)
    metadata = extract_metadata(target_path)
    archive_index.append(metadata)
    save_index(ARCHIVE_INDEX, archive_index)
    typer.secho(f"📚 Added to ARCHIVE/index.yml", fg=typer.colors.GREEN)
