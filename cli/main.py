# cli/main.py

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
from cli import new, run, devices, export, config, menu, info

app = typer.Typer(help="XTIM: CLI for experimental neuroscience workflows")

app.add_typer(new.app, name="new", help="Create new experiments from templates")
app.add_typer(run.app, name="run", help="Execute experiment runs")
app.add_typer(devices.app, name="devices", help="Manage hardware interfaces")
app.add_typer(export.app, name="export", help="Export experiment outputs")
app.add_typer(config.app, name="config", help="Edit or inspect system configuration")
app.add_typer(menu.app, name="menu", help="Launch the interactive XTIM menu")
app.add_typer(info.app, name="info", help="View metadata for experiments")

if __name__ == "__main__":
    app()
