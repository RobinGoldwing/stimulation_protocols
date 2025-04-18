# cli/tests/test_fpd.py

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from rich import print

DEFAULT_CSV = Path(__file__).parent.parent.parent / "config" / "pupil_positions.csv"

def run(csv_path: Path = None):
    """
    Analyze inter-frame intervals from a pupil_positions.csv file.
    If no path is given, uses the default in config/.
    """
    target = csv_path if csv_path else DEFAULT_CSV

    if not target.exists():
        print(f"[red]❌ File not found: {target}[/red]")
        return

    data = pd.read_csv(target)
    if "pupil_timestamp" not in data.columns:
        print("[red]❌ Column 'pupil_timestamp' not found in CSV.[/red]")
        return

    timestamps = data["pupil_timestamp"].values
    diffs = np.diff(timestamps)

    print(f"[cyan]Loaded {len(timestamps)} timestamps from {target}[/cyan]")
    print(f"⏱️  Mean frame duration: {np.mean(diffs):.4f} s")
    print(f"📉  Std deviation      : {np.std(diffs):.4f} s")
    print(f"📈  Max gap            : {np.max(diffs):.4f} s")
    print(f"📉  Min gap            : {np.min(diffs):.4f} s")
    print(f"🎞️  Approx. FPS        : {1.0 / np.mean(diffs):.2f} Hz")

    plt.figure(figsize=(8, 4))
    plt.hist(diffs, bins=50, color='skyblue', edgecolor='black')
    plt.title("Frame Duration Histogram")
    plt.xlabel("Frame interval (s)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.ion()
    plt.show(block=False)
    input("🔎 Press ENTER to close the plot and continue...")
    plt.close()
