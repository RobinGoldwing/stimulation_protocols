# cli/test.py

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
