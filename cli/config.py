# cli/config.py

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
import yaml
from pathlib import Path
from typing import Optional

app = typer.Typer(help="Manage XTIM configuration settings")

CONFIG_PATH = Path.home() / ".xtimrc.yml"

DEFAULT_CONFIG = {
    "default_template": "screen-stimulus",
    "recording_path": str(Path.home() / "xtim_recordings"),
    "default_export_format": "csv",
    "pupil_api": {
        "ip": "127.0.0.1",
        "port": 50020
    }
}

def load_config() -> dict:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)
    return DEFAULT_CONFIG.copy()

def save_config(config: dict):
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f)

@app.command("show")
def show():
    """
    Display current XTIM configuration.
    """
    config = load_config()
    typer.echo("XTIM configuration:")
    typer.echo(yaml.dump(config, sort_keys=False))

@app.command("set")
def set_key(
    key: str = typer.Argument(..., help="Configuration key to set (e.g. pupil_api.ip)"),
    value: str = typer.Argument(..., help="New value for the configuration key"),
):
    """
    Set a configuration value (nested keys supported via dot notation).
    """
    config = load_config()
    parts = key.split(".")
    ref = config
    for part in parts[:-1]:
        ref = ref.setdefault(part, {})
    ref[parts[-1]] = value
    save_config(config)
    typer.echo(f"Updated: {key} = {value}")

@app.command("reset")
def reset():
    """
    Reset the configuration file to default values.
    """
    save_config(DEFAULT_CONFIG.copy())
    typer.echo("Configuration has been reset to default values.")
