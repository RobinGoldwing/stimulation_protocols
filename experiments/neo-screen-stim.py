# experiments/neo-screen-stim.py

"""
XTIM NEO-Screen Protocol
Present visual stimuli with Pupil Labs NEO and LSL synchronization.
Now uses commons.py for timing and stimulus logging.
"""

import argparse
from pathlib import Path
import numpy as np
from psychopy import visual, core, event
from pylsl import StreamInfo, StreamOutlet
from pupil_labs.realtime_api.simple import discover_one_device
from experiments import commons as cm

# ─────────────────────────────────────────────
# CLI arguments
# ─────────────────────────────────────────────

parser = argparse.ArgumentParser(description="Run XTIM NEO-Screen stimulation protocol.")
parser.add_argument("path", type=str, help="Path to experiment folder")
args = parser.parse_args()

target = Path(args.path)
if not target.exists():
    print(f"[red]❌ Path not found: {target}[/red]")
    exit(1)

# ─────────────────────────────────────────────
# Parameters
# ─────────────────────────────────────────────

config = {
    "n_repeats": 2,
    "shuffle": True,
    "screen_index": 1,
    "stim_time": 1.0,
    "blank_time": 0.4,
    "drift_time": 1.0,
    "text_size": 40,
    "welcome_duration": 3.0,
    "goodbye_duration": 3.0
}

obj_dir = target / "OBJECTS"
stimuli = list((obj_dir / "pseudorandom").glob("*.tif")) if config["shuffle"] else list(obj_dir.glob("*.tif"))
stimuli = stimuli * config["n_repeats"]
if config["shuffle"]:
    np.random.shuffle(stimuli)

output_dir = target / "__output__"
output_dir.mkdir(parents=True, exist_ok=True)
order_file = output_dir / "order.txt"

# ─────────────────────────────────────────────
# Device and LSL setup
# ─────────────────────────────────────────────

print("🔌 Connecting to Pupil Labs NEO device...")
device = discover_one_device()
print("✅ Connected.")

lsl_info = StreamInfo("XTIMMarkers", "Markers", 1, 0, "string", "xtim_neo")
lsl_out = StreamOutlet(lsl_info)

# ─────────────────────────────────────────────
# PsychoPy setup
# ─────────────────────────────────────────────

win = visual.Window(
    fullscr=True,
    screen=config["screen_index"],
    color=(127, 127, 127),
    colorSpace="rgb255",
    monitor="testMonitor",
    units="pix",
    allowGUI=False
)

text = visual.TextStim(win, text="Press any key to start", height=config["text_size"], color="black")
drift_dot = visual.Circle(win, radius=10, fillColor="black", lineColor="black")
stim = visual.ImageStim(win)

# ─────────────────────────────────────────────
# Load welcome and goodbye images
# ─────────────────────────────────────────────

script_img_dir = target / "script-images"
welcome_img_path = next(script_img_dir.glob("welcome.*"), None)
goodbye_img_path = next(script_img_dir.glob("goodbye.*"), None)

welcome_image = visual.ImageStim(win, image=str(welcome_img_path)) if welcome_img_path else None
goodbye_image = visual.ImageStim(win, image=str(goodbye_img_path)) if goodbye_img_path else None

# ─────────────────────────────────────────────
# Show welcome screen or wait for key
# ─────────────────────────────────────────────

if welcome_image:
    for _ in range(int(config["welcome_duration"] * 60)):
        welcome_image.draw()
        win.flip()
else:
    text.draw()
    win.flip()

event.waitKeys()

# ─────────────────────────────────────────────
# Start stimulation session
# ─────────────────────────────────────────────

drift_dot.draw()
win.flip()
lsl_out.push_sample(["DRIFT"])
device.send_event("DRIFT")
core.wait(config["drift_time"])

device.recording_start()
lsl_out.push_sample(["START"])
device.send_event("START")
cm.tic("stim_loop")

print(f"🎞️  Presenting {len(stimuli)} images...")
order = []

for i, img in enumerate(stimuli):
    stim.image = str(img)
    stim.draw()
    win.flip()

    marker = f"stim_{i}"
    lsl_out.push_sample([marker])
    device.send_event(marker)
    order.append(img.name)

    win.getMovieFrame(buffer="back")
    screenshot = output_dir / f"{i:03d}_{img.name}"
    win.saveMovieFrames(str(screenshot))

    core.wait(config["stim_time"])
    win.flip()
    core.wait(config["blank_time"])

# ─────────────────────────────────────────────
# End of experiment and goodbye screen
# ─────────────────────────────────────────────

lsl_out.push_sample(["END"])
device.send_event("END")
core.wait(1.0)

duration = cm.toc("stim_loop")
recording_id = device.recording_stop_and_save()

# Save order and duration
cm.save_list_to_txt(order, order_file)
print(f"📝 Order saved to {order_file}")
print(f"✅ Duration: {duration:.2f} seconds")
print(f"🛑 Recording saved. ID: {recording_id}")

# Show goodbye image if available
if goodbye_image:
    for _ in range(int(config["goodbye_duration"] * 60)):
        goodbye_image.draw()
        win.flip()

win.close()
core.quit()
