# experiments/core-screen-stim.py

"""
XTIM Core-Screen Experiment Protocol
Stimulus presentation with full temporal and spatial logging,
Pupil Labs integration, and LSL annotation support.

Author: Rubén Álvarez-Mosquera
Project: XSCAPE / XTIM
"""

import os
import argparse
from pathlib import Path
from psychopy import visual, core, event
from pylsl import StreamInfo, StreamOutlet
import numpy as np
from datetime import datetime
from experiments import commons as cm

# ─────────────────────────────────────────────
# Argument parsing
# ─────────────────────────────────────────────

parser = argparse.ArgumentParser(description="Run XTIM Core-Screen stimulation protocol.")
parser.add_argument("path", type=str, help="Path to the experiment folder (LABORATORY/<name>)")
args = parser.parse_args()

target = Path(args.path)
if not target.exists():
    print(f"[red]❌ Path not found: {target}[/red]")
    exit(1)

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────

config = {
    "n_repeats": 2,
    "shuffle": True,
    "text_size": 40,
    "drift_color": "black",
    "screen_index": 1,
    "stim_time": 1.0,
    "blank_time": 0.4,
    "drift_time": 1.0
}

obj_dir = target / "OBJECTS"
order_file = target / "objects-output" / "order.txt"
screenshot_dir = target / "objects-output"
config_path = target / "config" / "display-conf.yml"

stimuli = list((obj_dir / "pseudorandom").glob("*.png")) if config["shuffle"] else list(obj_dir.glob("*.png"))
stimuli = stimuli * config["n_repeats"]
if config["shuffle"]:
    np.random.shuffle(stimuli)

# ─────────────────────────────────────────────
# Initialize devices
# ─────────────────────────────────────────────

print("🔌 Initializing communication...")
pupil_socket = cm.setup_pupil_remote_connection()
lsl_info = StreamInfo('XTIMMarkers', 'Markers', 1, 0, 'string', 'xtim_core')
lsl_out = StreamOutlet(lsl_info)

# ─────────────────────────────────────────────
# Prepare PsychoPy stimuli
# ─────────────────────────────────────────────

print("🖥️  Opening PsychoPy window...")
win = visual.Window(
    fullscr=True,
    screen=config["screen_index"],
    color=(127, 127, 127),
    colorSpace="rgb255",
    monitor="testMonitor",
    units="pix",
    allowGUI=False
)

drift_dot = visual.Circle(win, radius=10, fillColor=config["drift_color"], lineColor=config["drift_color"])
text = visual.TextStim(win, text="Press any key to start", height=config["text_size"], color="black")
image_stim = visual.ImageStim(win)

# ─────────────────────────────────────────────
# Welcome screen
# ─────────────────────────────────────────────

text.draw()
win.flip()
event.waitKeys()

# ─────────────────────────────────────────────
# DRIFT + START
# ─────────────────────────────────────────────

drift_dot.draw()
win.flip()
lsl_out.push_sample(["DRIFT"])
cm.new_annotation(pupil_socket, "DRIFT")
core.wait(config["drift_time"])

lsl_out.push_sample(["START"])
cm.new_annotation(pupil_socket, "START")
cm.tic("stimuli")

# ─────────────────────────────────────────────
# PRESENTATION LOOP
# ─────────────────────────────────────────────

print(f"🎞️  Presenting {len(stimuli)} images...")
order = []

for i, img in enumerate(stimuli):
    image_stim.image = str(img)
    image_stim.draw()
    win.flip()

    marker = f"stim_{i}"
    lsl_out.push_sample([marker])
    cm.new_annotation(pupil_socket, marker)
    order.append(img.name)

    screenshot = screenshot_dir / f"{i:03d}_{img.name}"
    win.getMovieFrame(buffer='back')
    win.saveMovieFrames(str(screenshot))

    core.wait(config["stim_time"])

    win.flip()
    core.wait(config["blank_time"])

# ─────────────────────────────────────────────
# ENDING
# ─────────────────────────────────────────────

lsl_out.push_sample(["END"])
cm.new_annotation(pupil_socket, "END")
duration = cm.toc("stimuli")

cm.save_list_to_txt(order, order_file)
print(f"✅ Experiment completed in {duration:.2f} seconds.")
win.close()
core.quit()
