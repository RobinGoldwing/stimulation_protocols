# cli/test.py

import typer
from pathlib import Path
from rich import print

app = typer.Typer(help="Run diagnostic or visual tests")

LAB_PATH = Path(__file__).parent.parent / "LABORATORY"
ARCHIVE_PATH = Path(__file__).parent.parent / "ARCHIVE"
EXPORTS_PATH = Path(__file__).parent.parent / "EXPORTS"

def resolve_experiment_path(name: str) -> Path:
    for base in [LAB_PATH, ARCHIVE_PATH]:
        path = base / name
        if path.exists():
            return path
    if (EXPORTS_PATH / name).exists():
        print(f"[red]❌ Cannot run test on '{name}' because it is archived as ZIP in EXPORTS/.[/red]")
        print(f"[dim]🛈 Please extract it manually to LABORATORY/ or ARCHIVE/ to test visual features.[/dim]")
    else:
        print(f"[red]❌ Experiment '{name}' not found in LABORATORY or ARCHIVE[/red]")
    raise typer.Exit()

@app.command("luminance")
def test_luminance(name: str = typer.Argument(..., help="Experiment name (LABORATORY or ARCHIVE)")):
    """
    Run luminance test using display-conf.yml from experiment.
    """
    from cli.tests import test_luminance as luminance
    exp_path = resolve_experiment_path(name)
    luminance.run(exp_path)

@app.command("frame-rate")
def test_framerate():
    """
    Measure the actual frame rate of the selected monitor.
    """
    from cli.tests import test_frame_rate as fr
    fr.run()

@app.command("tic-toc")
def test_tic_toc():
    """
    Basic timer check: prints elapsed time over 5 seconds.
    """
    from cli.tests import test_tic_toc as fr
    fr.run()

@app.command("fpd")
def test_fpd(
    file: Path = typer.Option(None, "--file", "-f", help="Optional path to pupil_positions.csv")
):
    """
    Run FPD analysis on a global or specified CSV file.
    """
    from cli.tests import test_fpd as fpd
    fpd.run(file)
