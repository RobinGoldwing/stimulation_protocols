# cli/run.py

import typer
from pathlib import Path
import subprocess
import sys

app = typer.Typer(help="Execute official XTIM experiments")

EXPERIMENT_SCRIPTS = {
    "core-screen": "core-screen-stim.py",
    "core-asset": "core-asset-stim.py",
    "neo-screen": "neo-screen-stim.py",
    "neo-asset": "neo-asset-stim.py"
}

EXPERIMENT_PATH = Path(__file__).parent.parent / "experiments"

@app.command("list")
def list_experiments():
    """
    List available predefined XTIM experiments.
    """
    typer.echo("📦 Available experiments:")
    for key in EXPERIMENT_SCRIPTS:
        typer.echo(f"  - {key}")

@app.command("start")
def start(
    name: str = typer.Argument(..., help="Name of the experiment to run"),
    path: Path = typer.Option(..., "--path", "-p", help="Path where assets/images should be saved"),
):
    """
    Start a predefined XTIM experiment.
    """
    if name not in EXPERIMENT_SCRIPTS:
        typer.echo(f"❌ Experiment '{name}' not found. Use 'xtim run list' to see available.")
        raise typer.Exit()

    script = EXPERIMENT_PATH / EXPERIMENT_SCRIPTS[name]
    if not script.exists():
        typer.echo(f"❌ Script not found: {script}")
        raise typer.Exit()

    command = [sys.executable, str(script), str(path)]
    typer.echo(f"🚀 Launching experiment: {name}")
    typer.echo(f"📁 Output path: {path}")
    typer.echo(f"▶ Command: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        typer.echo("✅ Experiment completed.")
    except subprocess.CalledProcessError as e:
        typer.echo(f"❌ Experiment failed: {e}")
        raise typer.Exit(code=1)
