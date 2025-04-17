
import typer
import subprocess
from pathlib import Path

app = typer.Typer(help="Interactive menu for scientific users")

LABS_PATH = Path("/neurolab/labs")


def run_live(command: list[str], description: str):
    typer.echo(f"\n🔧 {description}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in process.stdout:
        typer.echo(line.strip())

    process.wait()
    if process.returncode != 0:
        typer.secho(f"❌ Command exited with code {process.returncode}", fg=typer.colors.RED)


def list_labs():
    """Lista todos los laboratorios disponibles."""
    typer.echo(f"🔍 Buscando laboratorios en: {LABS_PATH}")
    if not LABS_PATH.exists():
        typer.echo("❌ El directorio de laboratorios no existe.")
        return

    labs = [p for p in LABS_PATH.iterdir() if p.is_dir()]
    if not labs:
        typer.echo("⚠️ No se encontraron laboratorios.")
        return

    for lab in labs:
        typer.echo(f"🧪 {lab.name}")

    
def list_experiments(lab: str):
    """
    Lista todos los experimentos existentes en un laboratorio dado.
    """
    path = LABS_PATH / lab / "experiments"

    typer.echo(f"\n🔬 Buscando experimentos en: {path}")

    if not path.exists() or not path.is_dir():
        typer.secho("❌ No se encontró el directorio de experimentos.", fg=typer.colors.RED)
        return

    experiments = [p for p in path.iterdir() if p.is_dir()]
    if not experiments:
        typer.echo("⚠️ No se encontraron experimentos en este laboratorio.")
        return

    for exp in experiments:
        typer.echo(f"🧪 {exp.name}")



@app.command("start")
def menu():
    typer.secho("\n🧠 Welcome to NeuroLabCore", fg=typer.colors.CYAN, bold=True)

    while True:
        typer.echo("\nChoose an option:")
        typer.echo("1. Create new lab")
        typer.echo("2. List labs")
        typer.echo("3. Create experiment in a lab")
        typer.echo("4. List experiments")
        typer.echo("5. Delete lab")
        typer.echo("6. Delete experiment")
        typer.echo("7. Export lab")
        typer.echo("8. Export experiment")
        typer.echo("9. Exit")

        try:
            choice = typer.prompt("Option", type=int)
        except typer.Abort:
            typer.echo("\nExiting.")
            raise typer.Exit()

        if choice == 1:
            name = typer.prompt("Enter lab name")
            run_live(["python", "-m", "cli.lab", "new", name], f"Creating lab '{name}'")
            list_labs()
        elif choice == 2:
            run_live(["python", "-m", "cli.lab", "list"], "Listing available labs")
        elif choice == 3:
            list_labs()
            lab = typer.prompt("Enter lab name")
            list_experiments(lab)
            exp = typer.prompt("Enter experiment name")
            run_live(["python", "-m", "cli.experiment", "create", "lab", lab, "name", exp],
                     f"Creating experiment '{exp}' in lab '{lab}'")
            list_experiments(lab)
        elif choice == 4:
            list_labs()
            lab = typer.prompt("Enter lab name")
            list_experiments(lab)
        elif choice == 5:
            list_labs()
            lab = typer.prompt("Enter lab name to delete")
            run_live(["python", "-m", "cli.lab", "delete", lab, "--force"], f"Deleting lab '{lab}'")
            list_labs()
        elif choice == 6:
            list_labs()
            lab = typer.prompt("Enter lab name")
            list_experiments(lab)
            exp = typer.prompt("Enter experiment name to delete")
            run_live(["python", "-m", "cli.experiment", "delete", "lab", lab, "name", exp],
                     f"Deleting experiment '{exp}' from lab '{lab}'")
            list_experiments(lab)
        elif choice == 7:
            list_labs()
            name = typer.prompt("Enter lab name to export")
            run_live(["python", "-m", "cli.export", "lab", name], f"Exporting lab '{name}'")
            typer.echo(f"📦 You can now copy it with:")
            typer.echo(f"docker cp neurolab-core:/tmp/export?¿?¿?¿?ed_labs/{name} ./downloads/{name}")
        elif choice == 8:
            list_labs()
            lab = typer.prompt("Enter lab name")
            list_experiments(lab)
            exp = typer.prompt("Enter experiment name to export")
            run_live(["python", "-m", "cli.export_exp", "lab", lab, "exp", exp], f"Exporting Experiment '{lab}' / {exp}")
            typer.echo(f"📦 You can now copy it with:")
            typer.echo(f"docker cp neurolab-core:/tmp/expor?¿?¿?¿?¿ted_labs/{name} ./downloads/{name}")
        elif choice == 9:
            typer.echo("👋 Goodbye!")
            raise typer.Exit()
        else:
            typer.echo("❌ Invalid option. Please try again.")
