# cli/tests/test_luminance.py

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

from psychopy import visual, core, event
from pathlib import Path
import yaml
import pyglet

def choose_monitor_index():
    try:
        screens = pyglet.canvas.get_display().get_screens()
        print("\nAvailable monitors:")
        for idx, s in enumerate(screens):
            print(f"  [{idx}] {s.width}x{s.height}")
        choice = input("Select monitor index (default 0): ")
        return int(choice) if choice.isdigit() and int(choice) < len(screens) else 0
    except Exception as e:
        print(f"[red]⚠ Could not detect monitors via pyglet: {e}[/red]")
        return 0

def run(experiment_path: Path):
    """
    Run a luminance flicker test using the display-conf.yml of the experiment.
    """
    config_path = experiment_path / "config" / "display-conf.yml"
    if not config_path.exists():
        print(f"[red]❌ Configuration file not found: {config_path}[/red]")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    mon_cfg = config.get("monitor", {})
    disp_cfg = config.get("display", {})

    resolution = mon_cfg.get("resolution", [1024, 768])
    refresh = mon_cfg.get("refresh_rate_hz", 60.0)
    fullscreen = disp_cfg.get("fullscreen", True)
    use_gui = disp_cfg.get("use_gui", False)
    bg = disp_cfg.get("color_rgb255", [127, 127, 127])
    color_space = disp_cfg.get("color_space", "rgb255")

    screen_index = choose_monitor_index()

    print(f"[cyan]🧪 Running luminance test with:[/cyan]")
    print(f"  Monitor index  : {screen_index}")
    print(f"  Resolution     : {resolution}")
    print(f"  Refresh Rate   : {refresh} Hz")
    print(f"  Background RGB : {bg}")
    print(f"  Fullscreen     : {fullscreen}")
    print(f"  Press any key or wait 5s to exit.")

    win = visual.Window(
        size=resolution,
        fullscr=True,
        color=tuple(bg),
        colorSpace=color_space,
        allowGUI=use_gui,
        monitor="testMonitor",
        units="pix",
        screen=screen_index
    )

    timer = core.CountdownTimer(5)
    while timer.getTime() > 0:
        win.flip()
        if event.getKeys():
            break

    win.close()
    core.quit()
