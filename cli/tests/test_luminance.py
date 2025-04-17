# cli/tests/luminance.py

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

from pathlib import Path
from psychopy import visual
import yaml

CONFIG_PATH = Path(__file__).parent.parent.parent / "config" / "display-conf.yml"

def load_display_config():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Display configuration file not found: {CONFIG_PATH}")
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def run():
    """
    Load display and monitor parameters from config/display-conf.yml and run a luminance stability test.
    The window flips continuously in a constant gray tone. Terminate manually (e.g., Alt+F4).
    """
    config = load_display_config()
    monitor_cfg = config.get("monitor", {})
    display_cfg = config.get("display", {})

    resolution = monitor_cfg.get("resolution", [1024, 768])
    screen = display_cfg.get("screen_index", 0)
    distance = monitor_cfg.get("distance_cm", 60)
    width = monitor_cfg.get("width_cm", 50)
    hz = monitor_cfg.get("refresh_rate_hz", 60.0)

    fullscreen = display_cfg.get("fullscreen", True)
    use_gui = display_cfg.get("use_gui", False)
    color = display_cfg.get("color_rgb255", [110, 110, 110])
    color_space = display_cfg.get("color_space", "rgb255")

    print(f"Launching luminance test with:")
    print(f"  Resolution     : {resolution}")
    print(f"  Refresh Rate   : {hz} Hz")
    print(f"  Distance       : {distance} cm")
    print(f"  Width          : {width} cm")
    print(f"  Fullscreen     : {fullscreen}")
    print(f"  Background RGB : {color}")

    win = visual.Window(
        size=resolution,
        screen=screen,
        units="pix",
        allowGUI=use_gui,
        fullscr=fullscreen,
        monitor=None,
        color=tuple(color),
        colorSpace=color_space,
    )

    while True:
        win.flip()
