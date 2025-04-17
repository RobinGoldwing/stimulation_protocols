# cli/test.py

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

import typer
from cli.tests import frame_rate, luminance, tic_toc, fpd

app = typer.Typer(help="Run diagnostic or calibration tests")

@app.command("frame-rate")
def test_frame_rate():
    """
    Measure actual frame rate of the display.
    """
    frame_rate.run()

@app.command("luminance")
def test_luminance():
    """
    Launch a luminance uniformity or flicker test.
    """
    luminance.run()

@app.command("tic-toc")
def test_tic_toc():
    """
    Test time measurement accuracy using tic() / toc().
    """
    tic_toc.run()

@app.command("fpd")
def test_fpd():
    """
    Plot frame duration distribution from pupil_positions.csv.
    """
    fpd.run()
