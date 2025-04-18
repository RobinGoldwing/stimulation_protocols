# cli/assets.py

import typer
from pathlib import Path
import shutil
import secrets
from rich import print, panel

app = typer.Typer(help="Generate, import, and shuffle assets.txt files for experiments")

VALID_EXTENSIONS = [".tif", ".tiff", ".png", ".jpg", ".jpeg"]
LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"

rand = secrets.SystemRandom()

def is_valid_asset(file: Path) -> bool:
    return file.suffix.lower() in VALID_EXTENSIONS

def resolve_experiment(name: str) -> Path:
    """Search LABORATORY or ARCHIVE for a given experiment name."""
    lab = LAB_PATH / name
    arc = ARCHIVE_PATH / name
    if lab.exists():
        return lab
    elif arc.exists():
        print(f"[red]❌ Experiment '{name}' is in ARCHIVE/. Move it to LABORATORY/ before proceeding.[/red]")
        raise typer.Exit()
    else:
        print(f"[red]❌ Experiment '{name}' not found in LABORATORY/ or ARCHIVE/[/red]")
        raise typer.Exit()

@app.command("gen")
def generate_assets(
    name: str = typer.Argument(..., help="Name of the experiment"),
    source: Path = typer.Option(None, "--from", "-f", help="Optional path to directory containing assets")
):
    """
    Generate assets.txt from a folder of stimuli.
    Filters for .tif/.png/.jpg/.jpeg only and stores only filenames (no extensions).
    """
    project = resolve_experiment(name)
    assets_folder = source if source else (project / "OBJECTS")
    assets_file = project / "assets.txt"

    if not assets_folder.exists():
        print(f"[red]❌ Folder not found: {assets_folder}[/red]")
        raise typer.Exit()

    files = sorted([f.stem for f in assets_folder.iterdir() if f.is_file() and is_valid_asset(f)])
    if not files:
        print(f"[yellow]⚠ No valid image files found in {assets_folder}[/yellow]")
        raise typer.Exit()

    rand.shuffle(files)

    with open(assets_file, "w", encoding="utf-8") as f:
        for name in files:
            f.write(name + "\n")

    print(f"[green]✅ assets.txt created at {assets_file} with {len(files)} entries.[/green]")

@app.command("random")
def shuffle_assets(
    name: str = typer.Argument(..., help="Name of the experiment")
):
    """
    Shuffle the lines in assets.txt using cryptographically secure random.
    """
    project = resolve_experiment(name)
    assets_file = project / "assets.txt"

    if not assets_file.exists():
        print(f"[red]❌ assets.txt not found at: {assets_file}[/red]")
        raise typer.Exit()

    with open(assets_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print(f"[yellow]⚠ assets.txt is empty[/yellow]")
        raise typer.Exit()

    rand.shuffle(lines)

    with open(assets_file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"[green]🔀 assets.txt at {assets_file} has been randomized.[/green]")

@app.command("import")
def import_assets(
    source: Path = typer.Option(..., "--from", "-f", help="Folder with images to import"),
    exp: str = typer.Option(..., "--exp", "-e", help="Name of the experiment to import into")
):
    """
    Import image assets into the OBJECTS/ folder of a LABORATORY experiment.
    """
    project = resolve_experiment(exp)
    objects_dir = project / "OBJECTS"
    objects_dir.mkdir(parents=True, exist_ok=True)

    if not source.exists():
        print(f"[red]❌ Source folder not found: {source}[/red]")
        raise typer.Exit()

    copied = 0
    for f in source.iterdir():
        if f.is_file() and is_valid_asset(f):
            shutil.copy2(f, objects_dir / f.name)
            copied += 1

    print(f"[green]📥 Imported {copied} image files into {objects_dir}[/green]")

    generate_assets(project, objects_dir)
    shuffle_assets(project)
