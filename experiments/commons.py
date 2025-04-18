# experiments/commons.py

"""
Commons Module for XTIM Experiments
Provides utilities for Pupil Labs control, timing, stimulus logging, and frame rate validation.
"""

import time
import os
import zmq
import requests
import json
from psychopy import visual, core

# ─────────────────────────────────────────────
# PATH & FILE UTILITY
# ─────────────────────────────────────────────

def save_list_to_txt(lista, filename):
    """
    Save a list of strings or values to a text file (one item per line).
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for item in lista:
            f.write(f"{item}")


# ─────────────────────────────────────────────
# PUPIL LABS INTERFACE (ZMQ)
# ─────────────────────────────────────────────

def check_capture_exists():
    """
    Check if Pupil Capture is running by attempting to connect to its REST API.
    Returns True if available, False otherwise.
    """
    try:
        r = requests.get("http://localhost:50020")
        return r.status_code == 200
    except requests.RequestException:
        return False

def setup_pupil_remote_connection():
    """
    Initialize ZMQ connection to Pupil Remote plugin on port 50020.
    Returns the socket object.
    """
    context = zmq.Context()
    pupil_remote = context.socket(zmq.REQ)
    pupil_remote.connect("tcp://127.0.0.1:50020")
    return pupil_remote

def request_pupil_time(pupil_socket):
    """
    Request the current time from Pupil Capture clock via ZMQ.
    Returns a float timestamp.
    """
    pupil_socket.send_string("t")
    pupil_time = pupil_socket.recv_string()
    return float(pupil_time)

def notify(pupil_socket, label, timestamp=None, duration=0.0, tags=[]):
    """
    Send an annotation message to Pupil Labs with optional timestamp and tags.
    """
    payload = {
        "topic": "annotation",
        "label": label,
        "duration": duration,
        "timestamp": timestamp if timestamp is not None else time.time(),
        "tags": tags
    }
    pupil_socket.send_string(f"notify.{json.dumps(payload)}")
    pupil_socket.recv_string()

def new_annotation(pupil_socket, label, tags=[]):
    """
    Create and send a new annotation with current timestamp.
    """
    ts = request_pupil_time(pupil_socket)
    notify(pupil_socket, label, timestamp=ts, tags=tags)


# ─────────────────────────────────────────────
# FRAME RATE VALIDATION
# ─────────────────────────────────────────────

def getActualFrameRate(monitor=0):
    """
    Launch a PsychoPy window on the specified monitor and measure the actual frame rate.
    """
    win = visual.Window(fullscr=True, screen=monitor, monitor="testMonitor")
    clock = core.Clock()
    frames = 120
    durations = []

    for _ in range(frames):
        win.flip()
        durations.append(clock.getTime())
        clock.reset()

    win.close()
    core.quit()

    avg = sum(durations) / len(durations)
    print(f"📊 Measured {frames} flips")
    print(f"🕒 Avg frame duration: {avg:.4f} s ≈ {1.0 / avg:.2f} Hz")


# ─────────────────────────────────────────────
# TIMING FUNCTIONS
# ─────────────────────────────────────────────

_tic_reference = {}

def tic(name="default"):
    """
    Start a named timer.
    """
    _tic_reference[name] = time.perf_counter()

def toc(name="default"):
    """
    Stop and report elapsed time for a named timer.
    Returns the duration in seconds.
    """
    if name not in _tic_reference:
        print(f"[TIMER ERROR] No tic() set for '{name}'")
        return None
    delta = time.perf_counter() - _tic_reference[name]
    print(f"⏱️  {name} elapsed: {delta:.6f} seconds")
    return delta
