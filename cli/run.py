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
LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"

def resolve_experiment_path(name: str) -> Path:
    lab = LAB_PATH / name
    arc = ARCHIVE_PATH / name

    if lab.exists():
        return lab
    elif arc.exists():
        typer.echo(f"[yellow]⚠ Experiment '{name}' is in ARCHIVE/. Please move it to LABORATORY/ to run.[/yellow]")
        raise typer.Exit(code=1)
    else:
        typer.echo(f"[red]❌ Experiment '{name}' not found in LABORATORY or ARCHIVE.[/red]")
        raise typer.Exit(code=1)

@app.command("list")
def list_experiments():
    """
    List available predefined XTIM experiments.
    """
    typer.echo("📦 Available experiments:")
    for key in EXPERIMENT_SCRIPTS:
        typer.echo(f"  - {key}")

@app.command("check")
def check_environment(
    name: str = typer.Argument(..., help="Name of the experiment to validate (e.g. core-screen)"),
    exp: str = typer.Option(..., "--exp", "-e", help="Experiment name inside LABORATORY or ARCHIVE")
):
    """
    Validate if the experiment environment is ready to launch.
    """
    if name not in EXPERIMENT_SCRIPTS:
        typer.echo(f"[red]❌ Unknown experiment: {name}[/red]")
        raise typer.Exit()

    exp_path = resolve_experiment_path(exp)
    script = EXPERIMENT_PATH / EXPERIMENT_SCRIPTS[name]

    checks = [script.exists(), exp_path.exists()]
    if not checks[0]:
        typer.echo(f"[red]❌ Script missing: {script}[/red]")
    if not checks[1]:
        typer.echo(f"[red]❌ Experiment folder missing: {exp_path}[/red]")

    # Specific checks
    if "screen" in name and not (exp_path / "OBJECTS").exists():
        typer.echo(f"[red]❌ Missing OBJECTS folder in: {exp_path}[/red]")

    if "asset" in name and not (exp_path / "assets.txt").exists():
        typer.echo(f"[red]❌ Missing assets.txt in: {exp_path}[/red]")

    if "core" in name:
        try:
            import zmq
            import requests
        except ImportError:
            typer.echo("[red]❌ Required libraries for Core (zmq, requests) not found.[/red]")

    if "neo" in name:
        try:
            from pupil_labs.realtime_api.simple import discover_one_device
            discover_one_device()
        except:
            typer.echo("[red]❌ NEO device not detected or library missing.[/red]")

    if all(checks):
        typer.echo(f"[green]✅ Environment ready for '{name}' in '{exp}'[/green]")

@app.command("start")
def start(
    name: str = typer.Argument(..., help="Name of the experiment to run (e.g. core-screen)"),
    path: Path = typer.Option(None, "--path", "-p", help="Manual path to assets (e.g. c:/experiment)"),
    exp: str = typer.Option(None, "--exp", "-e", help="Experiment name inside LABORATORY or ARCHIVE")
):
    """
    Start a predefined XTIM experiment.
    """
    if name not in EXPERIMENT_SCRIPTS:
        typer.echo(f"[red]❌ Experiment '{name}' not found. Use 'xtim run list' to see available.[/red]")
        raise typer.Exit()

    if path is None and exp is None:
        typer.echo("[red]❌ You must provide either --path or --exp[/red]")
        raise typer.Exit()

    output_path = path if path else resolve_experiment_path(exp)
    script = EXPERIMENT_PATH / EXPERIMENT_SCRIPTS[name]
    if not script.exists():
        typer.echo(f"[red]❌ Script not found: {script}[/red]")
        raise typer.Exit()

    command = [sys.executable, str(script), str(output_path)]
    typer.echo(f"🚀 Launching experiment: [bold]{name}[/bold]")
    typer.echo(f"📁 Output path: {output_path}")
    typer.echo(f"▶ Command: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        typer.echo("[green]✅ Experiment completed.[/green]")
    except subprocess.CalledProcessError as e:
        typer.echo(f"[red]❌ Experiment failed: {e}[/red]")
        raise typer.Exit(code=1)
