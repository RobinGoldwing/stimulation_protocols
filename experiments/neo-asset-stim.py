# experiments/neo-asset-stim.py

"""
XTIM NEO-Asset Stimulation Protocol
Manual visual stimulation with Pupil Labs NEO and LSL.
"""

import argparse
from pathlib import Path
import random
from time import sleep
from pylsl import StreamInfo, StreamOutlet
import keyboard
from experiments import commons as cm
from pupil_labs.realtime_api.simple import discover_one_device

# ─────────────────────────────────────────────
# Argumentos CLI
# ─────────────────────────────────────────────

parser = argparse.ArgumentParser(description="Run NEO-Asset stimulation protocol.")
parser.add_argument("path", type=str, help="Target experiment folder (LABORATORY/<name>)")
args = parser.parse_args()

target_dir = Path(args.path)
if not target_dir.exists():
    raise SystemExit("❌ Target directory does not exist.")
if any(target_dir.iterdir()):
    raise SystemExit("❌ Target directory is not empty.")
# ─────────────────────────────────────────────
# Parámetros
# ─────────────────────────────────────────────

stimulus_duration = 10  # seconds

assets_file = target_dir / "assets.txt"
if not assets_file.exists():
    raise SystemExit(f"❌ File not found: {assets_file}")

with open(assets_file, "r", encoding="utf-8") as f:
    assets = [line.strip() for line in f if line.strip()]

random.shuffle(assets)
print(f"📦 {len(assets)} assets loaded and shuffled.")

# ─────────────────────────────────────────────
# Inicializar NEO y LSL
# ─────────────────────────────────────────────

print("🔌 Connecting to Pupil Labs NEO device...")
device = discover_one_device()
print("✅ Connected.")

lsl_info = StreamInfo(name="XTIMMarkers", type="Markers", channel_count=1, channel_format="string", source_id="xtim_neo_asset")
lsl_out = StreamOutlet(lsl_info)
# ─────────────────────────────────────────────
# Esperar inicio manual
# ─────────────────────────────────────────────

while True:
    user_input = input('🧪 Type "start" to begin the experiment: ')
    if user_input.lower() == "start":
        print("▶ Starting stimulation...")
        sleep(2)
        break
    else:
        print("⚠️  Invalid input. Press CTRL+C to cancel.")
# ─────────────────────────────────────────────
# Estimulación manual por asset
# ─────────────────────────────────────────────

device.recording_start()
lsl_out.push_sample(["START"])
device.send_event("START")

for i, asset in enumerate(assets):
    print(f"[{i+1}/{len(assets)}] Present asset: {asset} and press ENTER to start stimulation.")

    while True:
        if keyboard.read_key() == "enter":
            cm.tic()
            print(f"📍 Recording asset: {asset}")
            device.send_event(asset)
            lsl_out.push_sample([asset])

            sleep(stimulus_duration)

            device.send_event("end_of_stimulation")
            lsl_out.push_sample(["end_of_stimulation"])
            cm.toc()
            break
        else:
            print("⌛ Waiting for ENTER... Press CTRL+C to cancel.")

lsl_out.push_sample(["END"])
device.send_event("END")
sleep(1)

recording_id = device.recording_stop_and_save()
print(f"🛑 Recording saved. ID: {recording_id}")
# ─────────────────────────────────────────────
# Guardar orden de estimulación
# ─────────────────────────────────────────────

output_file = target_dir / "assets.txt"
cm.save_list_to_txt(assets, output_file)
print(f"✅ Assets saved to {output_file}")
