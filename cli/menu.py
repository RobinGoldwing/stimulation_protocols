# cli/menu.py

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
import questionary
from pathlib import Path

from cli import new, run, devices, export, config, info, test

app = typer.Typer(help="Launch the XTIM interactive menu")

def main_menu():
    while True:
        choice = questionary.select(
            "Select an XTIM operation:",
            choices=[
                "1. Create new experiment",
                "2. Run experiment",
                "3. Run system tests",
                "4. Device control",
                "5. Export experiment results",
                "6. Configuration",
                "7. Experiment info",
                "0. Exit"
            ]
        ).ask()

        if choice.startswith("1"):
            handle_new()

        elif choice.startswith("2"):
            handle_run()

        elif choice.startswith("3"):
            handle_test()

        elif choice.startswith("4"):
            handle_devices()

        elif choice.startswith("5"):
            handle_export()

        elif choice.startswith("6"):
            config.show()

        elif choice.startswith("7"):
            handle_info()

        elif choice.startswith("0"):
            typer.echo("Exiting XTIM menu.")
            raise typer.Exit()

def handle_new():
    template = questionary.text("Enter template name (as in config/experiment-templates/):").ask()
    output = questionary.path("Choose output directory for the experiment:").ask()
    new.experiment(template=template, output_dir=Path(output), no_input=False)

def handle_run():
    experiment_path = questionary.path("Select experiment directory to run:").ask()
    config_file = questionary.path("Optional config file (leave blank to use default):").ask()
    interactive = questionary.confirm("Run in interactive mode?", default=False).ask()

    run.start(
        experiment_path=Path(experiment_path),
        config_file=Path(config_file) if config_file else None,
        interactive=interactive
    )

def handle_devices():
    choice = questionary.select(
        "Device control options:",
        choices=[
            "1. List LSL streams",
            "2. Start Pupil Capture recording",
            "3. Stop Pupil Capture recording",
            "4. Export Pupil Capture recording",
            "0. Back"
        ]
    ).ask()

    if choice.startswith("1"):
        devices.list_streams()
    elif choice.startswith("2"):
        devices.pupil_app.get_command("start")()
    elif choice.startswith("3"):
        devices.pupil_app.get_command("stop")()
    elif choice.startswith("4"):
        export_path = questionary.path("Optional custom export path:").ask()
        devices.pupil_app.get_command("export")(export_path=Path(export_path) if export_path else None)

def handle_test():
    test_choice = questionary.select(
        "Run a diagnostic test:",
        choices=[
            "1. Frame rate test",
            "2. Luminance test",
            "3. Tic/Toc time test",
            "4. FPD plot from CSV",
            "0. Back"
        ]
    ).ask()

    if test_choice.startswith("1"):
        test.test_frame_rate()
    elif test_choice.startswith("2"):
        test.test_luminance()
    elif test_choice.startswith("3"):
        test.test_tic_toc()
    elif test_choice.startswith("4"):
        test.test_fpd()

def handle_export():
    experiment_path = questionary.path("Experiment directory to export from:").ask()
    export_to = questionary.path("Destination folder for exported data:").ask()
    include_raw = questionary.confirm("Include raw data?", default=False).ask()
    include_logs = questionary.confirm("Include log files?", default=False).ask()
    export_format = questionary.select("Export format:", choices=["csv", "json", "zip", "hdf5"]).ask()

    export.export_results(
        experiment_dir=Path(experiment_path),
        destination=Path(export_to),
        include_raw=include_raw,
        include_logs=include_logs,
        format=export_format
    )

def handle_info():
    exp_path = questionary.path("Path to experiment folder:").ask()
    info.experiment_info(Path(exp_path))

@app.command("start")
def start():
    """
    Launch the XTIM interactive menu.
    """
    main_menu()
