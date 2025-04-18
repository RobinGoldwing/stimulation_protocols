# 🖼️ Asset-Based Experiments (XTIM)

Asset-based experiments are designed to present **image stimuli from disk** in controlled sequences. Ideal for cognitive and affective research requiring naturalistic or structured visual input.

---

## 📂 Script Location

The asset experiment scripts are located in:

```
experiments/
├── core-asset-stim.py    ← for Pupil Core setups
├── neo-asset-stim.py     ← for Pupil Neo setups
```

---

## 🧠 Purpose

These scripts display pre-rendered images in `.tiff` or `.png` format from the `script-images/` directory, supporting:

- Timed sequences
- Inter-stimulus intervals
- Display logging
- Synchronized triggers

---

## 🚀 Running an Asset Experiment

```bash
xtim run core-asset --exp proyect_name
xtim run neo-asset --exp proyect_name
```

Or manually:

```bash
python experiments/core-asset-stim.py
# or
python experiments/neo-asset-stim.py
```

---

## ⚙️ Configuration File

File: `config/experiment.toml`

```toml
[experiment]
type = "asset"
hardware = "core"  # or "neo"
stimulus_duration = 1.0
inter_stimulus_interval = 0.5
```

---

## 📂 Stimuli Folder

Images must be placed in:

```
my_experiment/script-images/
├── welcome.tiff
├── goodbye.tiff
├── stimulus_001.tiff
└── ...
```

Make sure filenames are valid and ordered correctly if sequencing matters.

---

## 🧪 Specific Features

- Loads high-resolution `.tiff` images
- Sends event markers to eye-tracking device
- Logs timestamps per stimulus
- Handles resolution and screen fitting automatically

---

## 🔬 Use Cases

- Image recognition
- Memory encoding/recall
- Visual categorization
- Affective image processing

---
