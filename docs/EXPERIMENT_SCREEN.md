# 🖥️ Screen-Based Experiments (XTIM)

Screen-based experiments in XTIM are designed for classical cognitive tasks where stimuli are displayed directly on a monitor, usually in full-screen mode, with precise timing and layout.

---

## 📂 Script Location

The screen experiment scripts are located in:

```
experiments/
├── core-screen-stim.py    ← for Pupil Core setups
├── neo-screen-stim.py     ← for Pupil Neo setups
```

---

## 🧠 Purpose

These scripts present **visual sequences** such as:

- Text messages (e.g., welcome/goodbye)
- Geometric stimuli (grids, cues, dots)
- Time-locked trials with fixation periods
- Custom screen layouts

---

## 🚀 Running a Screen Experiment

```bash
xtim run core-screen --exp proyect_name
xtim run neo-screen --exp proyect_name
```

XTIM will automatically select the appropriate script (Core or Neo) based on the `experiment.toml` configuration.

Alternatively, you can run directly for debugging:

```bash
python experiments/core-screen-stim.py
# or
python experiments/neo-screen-stim.py
```

---

## ⚙️ Configuration File

File: `config/experiment.toml`

```toml
[experiment]
type = "screen"
hardware = "neo"  # or "core"
duration = 300  # in seconds
fullscreen = true
```

---

## 🧪 Specific Features

- Uses PsychoPy or PyGame backend for precise timing
- Integrates with Pupil Capture for marker logging (if enabled)
- Timing logs and events are saved in `/log/`
- Visual confirmation for fixation and task transitions

---

## 🔬 Use Cases

- Reaction time tasks
- Working memory paradigms
- Visual search and attention
- Task switching and cueing

---
