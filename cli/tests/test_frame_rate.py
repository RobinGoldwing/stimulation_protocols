# cli/tests/test_frame_rate.py

import sys
import os
import pyglet

# =============================================================================
# XTIM – Experimental Toolkit for Multimodal Neuroscience
# =============================================================================
# Part of the XSCAPE Project (Experimental Science for Cognitive and Perceptual Exploration)
#
# Developed by:
#   - Arturo-José Valiño
#   - Rubén Álvarez-Mosquera
# =============================================================================

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if base_path not in sys.path:
    sys.path.insert(0, base_path)

from experiments import commons as cm

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

def run():
    """
    Measure the actual frame rate of the monitor using the commons module.
    """
    monitor_index = choose_monitor_index()
    cm.getActualFrameRate(monitor=monitor_index)
