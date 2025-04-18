# cli/delete.py

import typer
from pathlib import Path
import yaml
import shutil

app = typer.Typer(help="Delete experiments from the LABORATORY folder")

LAB_DIR = Path(__file__).parent.parent / "LABORATORY"
INDEX_FILE = LAB_DIR / "index.yml"

def load_index():
    if INDEX_FILE.exists():
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or []
    return []

def save_index(index):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(index, f, sort_keys=False)

@app.command("experiment")
def delete_experiment(
    name: str = typer.Argument(..., help="Name of the experiment to delete"),
    force: bool = typer.Option(False, "--force", "-f", help="Delete without confirmation"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be deleted without deleting"),
):
    """
    Delete an experiment and remove it from index.yml
    """
    exp_path = LAB_DIR / name

    if not exp_path.exists():
        typer.secho(f"❌ Experiment '{name}' not found in LABORATORY/", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    typer.echo(f"📁 Experiment path: {exp_path}")
    typer.echo(f"📓 Index file: {INDEX_FILE}")

    if dry_run:
        typer.secho("Dry run enabled — nothing will be deleted.", fg=typer.colors.YELLOW)
        return

    if not force:
        confirm = typer.confirm(f"Do you really want to delete experiment '{name}'?")
        if not confirm:
            typer.secho("❌ Aborted.", fg=typer.colors.RED)
            raise typer.Exit()

    # Delete folder
    try:
        shutil.rmtree(exp_path)
        typer.secho(f"✅ Folder deleted: {exp_path}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to delete folder: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=2)

    # Remove from index
    index = load_index()
    new_index = [entry for entry in index if entry.get("name") != name]
    if len(new_index) < len(index):
        save_index(new_index)
        typer.secho(f"📝 Entry removed from index.yml", fg=typer.colors.BLUE)
    else:
        typer.secho(f"⚠️ No entry found for '{name}' in index.yml", fg=typer.colors.YELLOW)
