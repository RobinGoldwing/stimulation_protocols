# cli/devices.py

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
import pylsl
import requests
from pathlib import Path

app = typer.Typer(help="Manage and test connected devices (LSL, Pupil Labs, Emobit, MilliKey)")

# -------------------------------------------------------------------
# Subcommand: xtim devices list
# -------------------------------------------------------------------
@app.command("list")
def list_streams(
    timeout: float = typer.Option(2.0, help="Timeout in seconds for LSL stream resolution"),
):
    """
    Discover and display all available LSL streams.
    """
    typer.echo("Searching for available LSL streams...")
    try:
        streams = pylsl.resolve_streams(wait_time=timeout)
        if not streams:
            typer.echo("No LSL streams found.")
            raise typer.Exit(code=0)

        for i, stream in enumerate(streams):
            typer.echo(f"[{i}] {stream.name()} ({stream.type()}) - {stream.hostname()}")
    except Exception as e:
        typer.echo(f"Error while resolving LSL streams: {e}")
        raise typer.Exit(code=1)

# -------------------------------------------------------------------
# Subcommand: xtim devices pupil start/stop/export
# -------------------------------------------------------------------
pupil_app = typer.Typer(help="Control Pupil Labs recording via API")
app.add_typer(pupil_app, name="pupil")

@pupil_app.command("start")
def start_recording(ip: str = "127.0.0.1", port: int = 50020):
    """
    Start a recording using the Pupil Capture API.
    """
    url = f"http://{ip}:{port}"
    try:
        requests.get(f"{url}/recording/start")
        typer.echo("Pupil Capture recording started.")
    except Exception as e:
        typer.echo(f"Failed to start recording: {e}")
        raise typer.Exit(code=1)

@pupil_app.command("stop")
def stop_recording(ip: str = "127.0.0.1", port: int = 50020):
    """
    Stop the ongoing recording in Pupil Capture.
    """
    url = f"http://{ip}:{port}"
    try:
        requests.get(f"{url}/recording/stop")
        typer.echo("Pupil Capture recording stopped.")
    except Exception as e:
        typer.echo(f"Failed to stop recording: {e}")
        raise typer.Exit(code=1)

@pupil_app.command("export")
def export_recording(ip: str = "127.0.0.1", port: int = 50020, export_path: Path = None):
    """
    Export the latest recording from Pupil Capture to a custom path.
    """
    url = f"http://{ip}:{port}"
    try:
        requests.get(f"{url}/export/manual")
        typer.echo("Pupil Capture export initiated.")

        if export_path:
            typer.echo(f"Note: custom export path requested -> {export_path}")
            # Currently Pupil Capture must be configured manually to change its export dir.
            # Advanced override via launch arguments or config patching would be required.
    except Exception as e:
        typer.echo(f"Failed to trigger export: {e}")
        raise typer.Exit(code=1)
