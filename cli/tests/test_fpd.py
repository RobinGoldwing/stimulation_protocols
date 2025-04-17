# cli/tests/fpd.py

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

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def run():
    """
    Load pupil_positions.csv and plot the frame-to-frame timestamp differences.
    Useful for diagnosing dropped frames or irregular frame durations.
    """
    csv_file = Path("pupil_positions.csv")
    if not csv_file.exists():
        print("pupil_positions.csv not found in current directory.")
        return

    data = pd.read_csv(csv_file)
    if "pupil_timestamp" not in data.columns:
        print("Column 'pupil_timestamp' not found in the CSV.")
        return

    ratio_frames = np.diff(data['pupil_timestamp'].values)

    plt.hist(ratio_frames, bins=50)
    plt.title("Frame Duration Distribution")
    plt.xlabel("Time between frames (s)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
