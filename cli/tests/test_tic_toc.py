# cli/tests/tic_toc.py

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

import sys
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if base_path not in sys.path:
    sys.path.insert(0, base_path)

from experiments import commons as cm

import time


def run():
    cm.tic()
    time.sleep(5)
    cm.toc()
