
# cli/new.py
import typer
from pathlib import Path
from cookiecutter.main import cookiecutter


import yaml
from datetime import datetime

def register_experiment_in_index(name: str, template_name: str, output_path: Path):
    index_path = LABORATORY_DIR / "index.yml"
    toml_file = output_path / "config" / "experiment.toml"

    entry = {
        "name": name,
        "created": datetime.now().isoformat(timespec="seconds"),
        "template": template_name
    }

    # Extraer datos del experiment.toml si existe
    if toml_file.exists():
        try:
            import toml
            exp_data = toml.load(toml_file)
            meta = exp_data.get("experiment", {})
            entry.update({
                "author": meta.get("author", "unknown"),
                "description": meta.get("description", ""),
                "version": meta.get("version", "0.1.0")
            })
        except Exception:
            pass  # Si falla, se registrará con info mínima

    # Cargar o crear index.yml
    if index_path.exists():
        with open(index_path, "r", encoding="utf-8") as f:
            index = yaml.safe_load(f) or []
    else:
        index = []

    index.append(entry)

    with open(index_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(index, f, sort_keys=False)

app = typer.Typer(help="Create a new experiment from a Cookiecutter template")

TEMPLATE_DIR = Path(__file__).parent.parent / "config" / "experiment-templates"
LABORATORY_DIR = Path(__file__).parent.parent / "LABORATORY"

@app.command("experiment")
def experiment(
    template: int = typer.Option(None, "--template", "-t", help="Number of the template to use"),
    name: str = typer.Argument(..., help="Name of the new experiment"),
):
    """
    Create a new experiment inside the LABORATORY/ directory using a selected Cookiecutter template.
    """
    # List available templates
    templates = [p for p in TEMPLATE_DIR.iterdir() if (p / "cookiecutter.json").exists()]
    if not templates:
        typer.echo("❌ No templates found in the template directory.")
        raise typer.Exit(code=1)

    # Prompt for selection if not given
    if template is None:
        typer.echo("📦 Available experiment templates:")
        for idx, tpl in enumerate(templates):
            typer.echo(f"[{idx}] {tpl.name}")
        template = typer.prompt("Enter the number of the template to use", type=int)

    if template < 0 or template >= len(templates):
        typer.echo("❌ Invalid template selection.")
        raise typer.Exit(code=1)

    selected_template = templates[template]
    output_path = LABORATORY_DIR / name

    LABORATORY_DIR.mkdir(parents=True, exist_ok=True)
    
    typer.echo(f"📁 Creating experiment '{name}' in {output_path}")
    try:
        cookiecutter(
            str(selected_template),
            output_dir=str(LABORATORY_DIR),
            no_input=False,
            extra_context={"experiment": name}
        )
        typer.echo("✅ Experiment created successfully.")
        register_experiment_in_index(name, selected_template.name, output_path)
    except Exception as e:
        typer.echo(f"❌ Error during experiment creation: {e}")
        raise typer.Exit(code=2)

@app.command("list")
def list_templates():
    """
    List available experiment templates.
    """
    if not TEMPLATE_DIR.exists():
        typer.echo("⚠️ No templates directory found.")
        return

    templates = [p.name for p in TEMPLATE_DIR.iterdir() if (p / "cookiecutter.json").exists()]
    if not templates:
        typer.echo("⚠️ No valid templates found.")
    else:
        typer.echo("📦 Available templates:")
        for t in templates:
            typer.echo(f" - {t}")
