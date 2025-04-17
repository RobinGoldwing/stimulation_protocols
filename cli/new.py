# cli/new.py

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
from pathlib import Path
from cookiecutter.main import cookiecutter

app = typer.Typer(help="Create a new experiment from a Cookiecutter template")

# Templates are expected to be in config/experiment-templates/{template}/
TEMPLATE_BASE_DIR = Path(__file__).parent.parent / "config" / "experiment-templates"

@app.command("experiment")
def experiment(
    template: str = typer.Argument(..., help="Name of the experiment template to use"),
    output_dir: Path = typer.Option(Path.cwd(), "--output-dir", "-o", help="Destination folder for the new experiment"),
    no_input: bool = typer.Option(False, "--no-input", help="Use default values without prompting"),
):
    """
    Create a new experiment using a named Cookiecutter template.
    Templates must be in: config/experiment-templates/{template}/
    """
    template_path = TEMPLATE_BASE_DIR / template
    if not template_path.exists() or not (template_path / "cookiecutter.json").exists():
        typer.echo(f"❌ Template '{template}' not found or invalid in {TEMPLATE_BASE_DIR}")
        raise typer.Exit(code=1)

    typer.echo(f"🚀 Using template: {template_path}")
    try:
        cookiecutter(
            str(template_path),
            output_dir=str(output_dir),
            no_input=no_input
        )
        typer.echo("✅ Experiment created successfully.")
    except Exception as e:
        typer.echo(f"❌ Error while creating experiment: {e}")
        raise typer.Exit(code=2)

@app.command("list")
def list_templates():
    """
    List available experiment templates.
    """
    if not TEMPLATE_BASE_DIR.exists():
        typer.echo("⚠️ No templates directory found.")
        return

    templates = [p.name for p in TEMPLATE_BASE_DIR.iterdir() if (p / "cookiecutter.json").exists()]
    if not templates:
        typer.echo("⚠️ No valid templates found.")
    else:
        typer.echo("📦 Available templates:")
        for t in templates:
            typer.echo(f" - {t}")
