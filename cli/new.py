# cli/new.py

import typer
from pathlib import Path
from cookiecutter.main import cookiecutter

app = typer.Typer(help="Create a new experiment from a Cookiecutter template")

TEMPLATE_DIR = Path(__file__).parent.parent / "config" / "experiment-templates"

@app.command("experiment")
def experiment(
    template: str = typer.Argument(..., help="Name of the experiment template to use"),
    output_dir: Path = typer.Option(Path.cwd(), "--output-dir", "-o", help="Destination folder for the new experiment"),
    no_input: bool = typer.Option(False, "--no-input", help="Use default values without prompting"),
):
    """
    Create a new experiment using a Cookiecutter template.
    """
    template_path = TEMPLATE_DIR / template
    if not template_path.exists():
        typer.echo(f"Template '{template}' not found in {TEMPLATE_DIR}")
        raise typer.Exit(code=1)

    typer.echo(f"Using template: {template_path}")
    try:
        cookiecutter(str(template_path), output_dir=str(output_dir), no_input=no_input)
        typer.echo(f"Experiment successfully created at: {output_dir}")
    except Exception as e:
        typer.echo(f"Error while creating experiment: {e}")
        raise typer.Exit(code=1)
