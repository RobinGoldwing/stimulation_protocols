
# cli/main.py

import typer

app = typer.Typer(
    help="XTIM: CLI for Experimental Neuroscience Workflows",
    epilog="""
Developed as part of the XSCAPE Project (INCIPIT/CSIC).
Designed to manage, execute and document multimodal cognitive science experiments
involving eye-tracking, physiological sensors, and real-time data streams.

For more info, visit: https://www.xscapeuos.com/

Author Contact:  

Arturo-Jose Valiño (Lead) : arturo-jose.valino@incipit.csic.es
    """
)

# Define lazy loading functions for each command group
def lazy_new(): from cli import new; return new.app
def lazy_run(): from cli import run; return run.app
def lazy_devices(): from cli import devices; return devices.app
def lazy_export(): from cli import export; return export.app
def lazy_config(): from cli import config; return config.app
def lazy_menu(): from cli import menu; return menu.app
def lazy_info(): from cli import info; return info.app
def lazy_doctor(): from cli import doctor; return doctor.app
def lazy_validate(): from cli import validate; return validate.app
def lazy_delete(): from cli import delete; return delete.app
def lazy_export(): from cli import export; return export.app
def lazy_archive(): from cli import archive; return archive.app
def lazy_test(): from cli import test; return test.app
def lazy_assets(): from cli import assets; return assets.app



# Register subcommands using lazy loaders
app.add_typer(lazy_new(), name="new", help="Create new experiments from standardized templates (Cookiecutter)")
app.add_typer(lazy_run(), name="run", help="Execute experimental sessions with real-time synchronization")
app.add_typer(lazy_devices(), name="devices", help="Configure and list available hardware interfaces")
app.add_typer(lazy_export(), name="export", help="Export experimental data and metadata for analysis or archiving")
app.add_typer(lazy_config(), name="config", help="Edit or inspect system-wide experimental configuration")
app.add_typer(lazy_menu(), name="menu", help="Launch the interactive XTIM terminal menu")
app.add_typer(lazy_info(), name="info", help="View and summarize experiment metadata and settings")
app.add_typer(lazy_doctor(), name="doctor", help="Run diagnostic checks for XTIM environment")
app.add_typer(lazy_validate(), name="validate", help="Validate experiment structure and metadata")
app.add_typer(lazy_delete(), name="delete", help="Delete experiments from LABORATORY")
app.add_typer(lazy_export(), name="export", help="Export experiments as compressed archives")
app.add_typer(lazy_archive(), name="archive", help="Archive experiments into the ARCHIVE folder")
app.add_typer(lazy_test(), name="test", help="Run integrated system tests")
app.add_typer(lazy_assets(), name="assets", help="Manage and generate assets.txt files for experiments")


if __name__ == "__main__":
    app()
