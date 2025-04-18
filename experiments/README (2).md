# XTIM Experimental Protocols

This document summarizes the four official experimental protocols included in the **XTIM** (Experimental Toolkit for Integrated Multimodal Neuroscience) system, developed as part of the **XSCAPE** research infrastructure.

All protocols can be executed via the CLI:

```bash
xtim run start <protocol-name> --exp <experiment-name>
```

---

## 🧪 Protocol Comparison

| Protocol         | Script                 | Device        | Mode         | Stimulus Source         | Sync Tools        | Assets Used     |
|------------------|------------------------|---------------|--------------|--------------------------|-------------------|------------------|
| `core-screen`    | `core-screen-stim.py`  | Pupil Core    | Automatic    | `OBJECTS/*.png`          | Pupil (ZMQ), LSL  | Stimuli only     |
| `core-asset`     | `core-asset-stim.py`   | Pupil Core    | Manual       | `assets.txt` (user input)| Pupil (pyplr), LSL| Annotated assets |
| `neo-screen`     | `neo-screen-stim.py`   | Pupil NEO     | Automatic    | `OBJECTS/*.tif`          | NEO API, LSL      | Stimuli only     |
| `neo-asset`      | `neo-asset-stim.py`    | Pupil NEO     | Manual       | `assets.txt` (user input)| NEO API, LSL      | Annotated assets |

---

## 🧠 Notes

- All protocols store:
  - Frame captures in `objects-output/`
  - Ordered list of stimuli in `order.txt` or `assets.txt`
  - Pupil annotations via each system’s compatible API
- Asset protocols (`*-asset`) require the user to press `ENTER` to advance, enabling synchronized marking of manually observed events
- Screen protocols (`*-screen`) are pseudo-randomized and time-controlled

---

## 🧰 Requirements

- `psychopy`, `pylsl`, `pyplr` (for core)
- `pupil-labs-realtime-api` (for NEO)
- `keyboard`, `numpy`, `matplotlib`, `zmq`, `requests`

---

## 🧾 Authors

Developed by the XSCAPE project.

XTIM integrates stimulus presentation, timestamped logging, and synchronization with eye tracking and biosignal devices for precision neuroscience.

---

## 📂 Directory structure

```
LABORATORY/
  demo001/
    OBJECTS/
    config/
    assets.txt
    objects-output/
```
