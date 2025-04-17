# cli/main.py

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
