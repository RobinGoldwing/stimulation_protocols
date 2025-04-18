# experiments/core-asset-stim.py

"""
XTIM Core-Asset Stimulation Protocol
Manual visual stimulation with Pupil Core and LSL.
"""

import argparse
from pathlib import Path
import random
from time import sleep
from pylsl import StreamInfo, StreamOutlet
from psychopy import core
import commons as cm
from pyplr.pupil import PupilCore
import keyboard
# ─────────────────────────────────────────────
# Argumentos CLI
# ─────────────────────────────────────────────

parser = argparse.ArgumentParser(description="Run Core-Asset stimulation protocol with Pupil Core and LSL.")
parser.add_argument("path", type=str, help="Target directory for saving results")
args = parser.parse_args()

target_dir = Path(args.path)
if not target_dir.exists():
    raise SystemExit("❌ Target directory does not exist.")
if any(target_dir.iterdir()):
    raise SystemExit("❌ Target directory is not empty.")
# ─────────────────────────────────────────────
# Inicialización
# ─────────────────────────────────────────────

stimulus_duration = 10  # seconds

info = StreamInfo(name="DataSyncMarker", type="Tags", channel_count=1,
                  channel_format="string", source_id="xtim_core_asset")
outlet = StreamOutlet(info)

cm.check_capture_exists(ip_address='127.0.0.1', port=50020)
p = PupilCore()

assets_file = target_dir / "assets.txt"
if not assets_file.exists():
    raise SystemExit(f"❌ File not found: {assets_file}")

with open(assets_file, "r", encoding="utf-8") as f:
    assets = [line.strip() for line in f if line.strip()]

random.shuffle(assets)
print(f"📦 {len(assets)} assets loaded and shuffled.")

# ─────────────────────────────────────────────
# Iniciar plugins y grabación
# ─────────────────────────────────────────────

p.command("R")
p.notify({"subject": "start_plugin", "name": "Annotation_Capture", "args": {}})
# Esperar confirmación de inicio
while True:
    user_input = input('🧪 Type "start" to begin the experiment: ')
    if user_input.lower() == "start":
        print("▶ Starting stimulation...")
        sleep(2)
        break
    else:
        print("⚠️  Invalid input. Press CTRL+C to cancel.")
# ─────────────────────────────────────────────
# Bucle de estimulación
# ─────────────────────────────────────────────

for i, asset in enumerate(assets):
    print(f"[{i+1}/{len(assets)}] Present asset: {asset} and press ENTER when ready.")

    while True:
        if keyboard.read_key() == "enter":
            cm.tic()
            print(f"📍 Recording asset: {asset}")
            annotation = p.new_annotation(asset)
            p.send_annotation(annotation)
            outlet.push_sample([asset])

            sleep(stimulus_duration)

            annotation = p.new_annotation("end_of_stimulation")
            p.send_annotation(annotation)
            outlet.push_sample(["end_of_stimulation"])

            cm.toc()
            break
        else:
            print("⚠️  Waiting for ENTER... Press CTRL+C to abort.")
# Final del experimento
outlet.push_sample(["end_of_experiment"])

while True:
    end_input = input('🧪 Type "f" to finish the experiment: ')
    if end_input.lower() == "f":
        print("🛑 Ending experiment...")
        break
    else:
        print("⚠️  Invalid input. Press CTRL+C to cancel.")

p.command("r")
# Guardar orden de assets
cm.save_list_to_txt(assets, target_dir / "assets.txt")
print(f"✅ Assets saved to {target_dir / 'assets.txt'}")
