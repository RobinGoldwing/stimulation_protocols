# cli/run.py

import typer
from pathlib import Path
import subprocess
import sys
import yaml

app = typer.Typer(help="Execute experiment runs from a configured folder")

DEFAULT_SCRIPT_NAME = "experiment.py"
DEFAULT_CONFIG_NAME = "config.yml"

@app.command("start")
def start(
    experiment_path: Path = typer.Argument(..., help="Path to the experiment run directory"),
    config_file: Path = typer.Option(None, "--config", "-c", help="Optional configuration file (default: config/config.yml)"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Run in interactive mode"),
):
    """
    Run an experiment from a given folder. Executes the default experiment script.
    """
    if not experiment_path.exists():
        typer.echo(f"Experiment path not found: {experiment_path}")
        raise typer.Exit(code=1)

    script_path = experiment_path / "scripts" / DEFAULT_SCRIPT_NAME
    if not script_path.exists():
        typer.echo(f"Experiment script not found: {script_path}")
        raise typer.Exit(code=1)

    config_path = config_file or (experiment_path / "config" / DEFAULT_CONFIG_NAME)
    if not config_path.exists():
        typer.echo(f"Configuration file not found: {config_path}")
        raise typer.Exit(code=1)

    typer.echo(f"Loading configuration from {config_path}")
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        typer.echo(f"Error reading configuration: {e}")
        raise typer.Exit(code=1)

    command = [sys.executable, str(script_path), "--config", str(config_path)]

    if interactive:
        command.append("--interactive")

    typer.echo(f"Executing experiment: {script_path}")
    try:
        subprocess.run(command, check=True)
        typer.echo("Experiment run completed.")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Experiment run failed: {e}")
        raise typer.Exit(code=1)
