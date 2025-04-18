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
  - Frame captures in `__output__/`
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

# ▶️ Running Experiments with XTIM

This guide explains how to properly configure, execute, and monitor experiments using the `xtim` framework.

---

## 🧩 Prerequisites

Before running any experiment, make sure you have:

- Installed the `xtim` system (`pip install -e .`)
- Activated the correct Conda environment (`conda activate xtim`)
- Created a valid experiment using `xtim new`
- Verified assets and device connections (optional but recommended)

---

## 🚀 Basic Command

To run an experiment:

```bash
xtim run
```

This command will automatically detect the experiment type, load the configuration files, and execute the presentation script.

---

## 🛠️ Optional Parameters

You can pass optional flags to customize execution:

| Option                   | Description                                    | Example                         |
|--------------------------|------------------------------------------------|----------------------------------|
| `--mode [asset|screen]`  | Choose presentation type                       | `xtim run --mode asset`         |
| `--experiment NAME`      | Run a specific experiment folder               | `xtim run --experiment exp001`  |
| `--config PATH`          | Provide a custom configuration file            | `xtim run --config my.toml`     |
| `--simulate`             | Dry-run mode (no real hardware, test only)     | `xtim run --simulate`           |

---

## 📂 Experiment Folder Structure

Each experiment has the following structure:

```
my_experiment/
├── config/
│   ├── display-conf.yml       ← visual display parameters
│   └── experiment.toml        ← main configuration file
├── __data__/                  ← output data
├── __models__/                ← models
├── __notebooks__/             ← jupyter notebooks
├── __results__/               ← Results
├── __output__/                ← processed results (optional)
├── script-images/             ← media Script files (TIFF, PNG)
├── OBJECTS/                   ← media Experiment files (TIFF, PNG)
├── log/                       ← runtime logs
├── scripts/                   ← custom Python routines
└── README.md                  ← Info about the experiment
```

---

## 📋 Typical Workflow Example

```bash
# Step 1: Create a new experiment
xtim new

# Step 2: (Optional) Customize the config
nano my_experiment/config/experiment.toml

# Step 3: Validate device and asset readiness
xtim devices test
xtim assets validate

# Step 4: Select your Experiment from a list
xtim run list

# Step 5: Run the experiment
xtim run --exp my_experiment

# Step 5: Check data and logs
ls my_experiment/data/
cat my_experiment/log/runtime.log
```

---

## 🧠 Scientific Tips

- Use **simulate mode** before real sessions to debug scripts
- Enable logging to track timing precision
- Archive experiments using `xtim archive` after completion
- Version control your experiment folders

---

## ❓ Troubleshooting

- **Missing config file?** → Make sure `experiment.toml` exists in `/config/`
- **Display not responding?** → Verify display setup in `display-conf.yml`
- **Crash at start?** → Run `xtim doctor` to test FPS and device bindings
- **Incorrect image rendering?** → Confirm your stimuli are in `.tiff` or `.png` format with correct resolution

---

## 🔄 Related Commands

- `xtim new` → Create a new experiment structure
- `xtim assets validate` → Ensure stimuli images are valid
- `xtim doctor` → Run diagnostics
- `xtim archive` → Save and compress experiment folder

---
