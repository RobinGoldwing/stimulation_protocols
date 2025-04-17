# cli/info.py

import typer
from pathlib import Path
import yaml
from datetime import datetime

app = typer.Typer(help="Display metadata and summary information for an experiment folder")

@app.command("experiment")
def experiment_info(
    experiment_path: Path = typer.Argument(..., help="Path to the experiment run directory"),
):
    """
    Show summary information about an experiment directory: subject, session date,
    available data, logs, results, and configuration parameters.
    """
    if not experiment_path.exists() or not experiment_path.is_dir():
        typer.echo(f"Experiment path does not exist or is not a directory: {experiment_path}")
        raise typer.Exit(code=1)

    typer.echo(f"Experiment directory: {experiment_path}")

    # Subject metadata
    subject_file = experiment_path / "subject_info.yml"
    if subject_file.exists():
        try:
            subject_data = yaml.safe_load(subject_file.read_text())
            typer.echo(f"Subject ID: {subject_data.get('id', 'N/A')}")
            typer.echo(f"Age: {subject_data.get('age', 'N/A')}")
            typer.echo(f"Condition: {subject_data.get('condition', 'N/A')}")
        except Exception as e:
            typer.echo(f"Failed to parse subject_info.yml: {e}")
    else:
        typer.echo("No subject_info.yml file found.")

    # Check for experiment script
    script_path = experiment_path / "scripts" / "experiment.py"
    typer.echo(f"Experiment script: {'✔️' if script_path.exists() else 'Missing'}")

    # Check for config
    config_path = experiment_path / "config" / "config.yml"
    typer.echo(f"Configuration file: {'✔️' if config_path.exists() else 'Missing'}")

    # Check for data
    raw_data = experiment_path / "data" / "raw"
    processed_data = experiment_path / "data" / "processed"
    typer.echo(f"Raw data: {'✔️' if raw_data.exists() else 'Missing'}")
    typer.echo(f"Processed data: {'✔️' if processed_data.exists() else 'Missing'}")

    # Check for results
    results = experiment_path / "results"
    typer.echo(f"Results: {'✔️' if results.exists() else 'Missing'}")

    # Check for logs
    log_path = experiment_path / "log"
    typer.echo(f"Log files: {'✔️' if log_path.exists() else 'Missing'}")

    # Last modified time
    last_modified = datetime.fromtimestamp(experiment_path.stat().st_mtime)
    typer.echo(f"Last modified: {last_modified.strftime('%Y-%m-%d %H:%M:%S')}")
