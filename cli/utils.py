# cli/utils.py

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

import yaml
from pathlib import Path
from typing import Union, Optional
import platform
import sys
import typer

def load_yaml(path: Union[str, Path]) -> dict:
    """
    Load a YAML file and return its contents as a dictionary.
    """
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        typer.echo(f"Failed to load YAML from {path}: {e}")
        return {}

def save_yaml(path: Union[str, Path], data: dict):
    """
    Save a dictionary as a YAML file.
    """
    try:
        with open(path, "w") as f:
            yaml.dump(data, f, sort_keys=False)
    except Exception as e:
        typer.echo(f"Failed to write YAML to {path}: {e}")

def validate_directory(path: Path, must_exist: bool = True) -> bool:
    """
    Validate that a directory exists (or optionally, that it can be created).
    """
    if must_exist:
        return path.exists() and path.is_dir()
    else:
        try:
            path.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            typer.echo(f"Cannot create directory {path}: {e}")
            return False

def resolve_config_path(experiment_dir: Path, filename: str = "config.yml") -> Optional[Path]:
    """
    Resolve a configuration file within an experiment directory.
    """
    config_path = experiment_dir / "config" / filename
    if config_path.exists():
        return config_path
    return None

def get_system_info() -> dict:
    """
    Return information about the system environment.
    """
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": sys.version,
        "platform": platform.platform()
    }

def format_title(title: str) -> str:
    """
    Return a formatted title string.
    """
    return f"\n{'=' * len(title)}\n{title}\n{'=' * len(title)}"
