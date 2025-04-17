# cli/tests/tic_toc.py

import time
import commons as cm

def run():
    cm.tic()
    time.sleep(5)
    cm.toc()
