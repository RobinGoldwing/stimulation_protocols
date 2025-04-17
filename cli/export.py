# cli/export.py

import typer
from pathlib import Path
import shutil
import os

app = typer.Typer(help="Export experiment data and results")

@app.command("results")
def export_results(
    experiment_dir: Path = typer.Argument(..., help="Path to the experiment folder"),
    destination: Path = typer.Option(..., "--to", "-t", help="Destination directory for exported results"),
    include_raw: bool = typer.Option(False, "--include-raw", help="Include raw data in export"),
    include_logs: bool = typer.Option(False, "--include-logs", help="Include log files in export"),
    format: str = typer.Option("csv", "--format", "-f", help="Export format: csv | json | hdf5 | zip"),
):
    """
    Export data and results from a completed experiment.
    """
    if not experiment_dir.exists():
        typer.echo(f"Experiment directory not found: {experiment_dir}")
        raise typer.Exit(code=1)

    result_dir = experiment_dir / "results"
    if not result_dir.exists():
        typer.echo(f"No results found in: {result_dir}")
        raise typer.Exit(code=1)

    destination.mkdir(parents=True, exist_ok=True)

    typer.echo(f"Exporting results from {experiment_dir} to {destination} as format '{format}'")

    try:
        if format == "zip":
            archive_path = shutil.make_archive(
                base_name=str(destination / experiment_dir.name),
                format="zip",
                root_dir=experiment_dir
            )
            typer.echo(f"Exported ZIP archive to {archive_path}")
            return

        for subdir in ["results"]:
            src = experiment_dir / subdir
            dst = destination / experiment_dir.name / subdir
            if src.exists():
                shutil.copytree(src, dst, dirs_exist_ok=True)

        if include_raw:
            raw = experiment_dir / "data" / "raw"
            dst = destination / experiment_dir.name / "data" / "raw"
            if raw.exists():
                shutil.copytree(raw, dst, dirs_exist_ok=True)

        if include_logs:
            logs = experiment_dir / "log"
            dst = destination / experiment_dir.name / "log"
            if logs.exists():
                shutil.copytree(logs, dst, dirs_exist_ok=True)

        typer.echo("Export completed successfully.")
    except Exception as e:
        typer.echo(f"Export failed: {e}")
        raise typer.Exit(code=1)
