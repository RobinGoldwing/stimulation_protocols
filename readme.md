# XTIM – Experimental Toolkit for Multimodal Cognitive Research

**XTIM** is a scientific framework developed to facilitate experimental research in human cognition and neuroscience. Created within the [XSCAPE Project](https://www.incipit.csic.es/en/project/xscape) by CSIC-INCIPIT, it provides a robust, modular CLI for designing, running, and managing multimodal experiments involving **eye-tracking**, **EEG**, **physiological sensors**, and **behavioral response systems**.

---

## 🧠 Scientific Motivation

In contemporary cognitive science and experimental psychology, the need for **synchronized multimodal data collection** is more critical than ever. XTIM addresses this need by offering a **command-line-based orchestration system** capable of:

- Presenting complex visual stimuli
- Recording behavioral and physiological data
- Coordinating across devices with microsecond-level accuracy
- Enabling structured metadata and reproducibility

XTIM supports cognitive tasks that require precision timing, dynamic environments, and flexible design — serving studies on **attention**, **perception**, **learning**, **sensorimotor integration**, and **decision-making**.

---

## ⚙️ Architecture Overview

XTIM is structured into modular components, all accessible via a unified CLI powered by [Typer](https://typer.tiangolo.com/). Key features include:

- **Cookiecutter Templates** for creating fully structured experiments
- **Configuration system** using TOML/YAML files
- **Integration** with Pupil Labs eye trackers, Emobit, MilliKey, and LSL
- **Device manager**, asset tools, menu system, export and archive utilities
- **Cross-platform** support via shell and PowerShell installers

---

## 🔬 Scientific Devices Supported

| Device / Interface | Description |
|--------------------|-------------|
| **Pupil Labs (Core & Neo)** | High-precision binocular eye tracking |
| **Emobit** | Wearable physiological monitoring (HR, GSR, etc.) |
| **MilliKey MH5** | Scientific button box with TTL, USB-HID |
| **LSL (Lab Streaming Layer)** | Real-time multimodal data synchronization |

XTIM allows hybrid device integration for experiments requiring low-latency synchronization.

---

## 🧪 Use Cases

XTIM supports a wide range of experimental designs:

- Visual stimuli in screen-based cognitive tests
- Scene-based exploration in head-mounted displays
- Reaction-time studies with precise stimulus-response control
- Emotional/physiological response mapping
- Neurophenomenology experiments using multimodal datasets

---

## 📦 Installation Guide

1. Clone the repository:

```bash
git clone https://github.com/Rockyneuron/stimulation_protocols
cd stimulation_protocols
```

2. Create the Conda environment:

```bash
conda env create -f config/conda-env/xtim-config-env.yml
conda activate xtim
```

3. Install the package:

```bash
pip install -e .
```

Or use:

```bash
bash install-xtim.sh        # Unix/macOS

./install-xtim.ps1          # Windows (PowerShell)
```

---
## 🧰 Command Summary + Usage Examples

The following table summarizes all available CLI commands in `xtim` and includes usage examples for common tasks.

| Command          | Description                                                            | Example Usage                                   |
|------------------|------------------------------------------------------------------------|--------------------------------------------------|
| `xtim new`       | Create a new experiment using a Cookiecutter template                  | `xtim new`                                       |
| `xtim run`       | Run an experiment (asset or screen based)                              | `xtim run` or `xtim run --mode asset`            |
| `xtim config`    | View or edit experiment configuration (TOML, YAML)                     | `xtim config show`                               |
| `xtim devices`   | List, test, or initialize connected scientific devices                 | `xtim devices list`                              |
| `xtim assets`    | Verify, list, or test media files used in stimuli                      | `xtim assets validate`                           |
| `xtim menu`      | Launch an interactive text-based menu                                  | `xtim menu`                                      |
| `xtim export`    | Export experiment results or configuration as a ZIP or folder          | `xtim export --format zip`                       |
| `xtim archive`   | Archive a completed experiment, moving it to an archive folder         | `xtim archive my_experiment`                     |
| `xtim doctor`    | Run system diagnostics, dependency checks, and FPS/luminance tests     | `xtim doctor` or `xtim doctor --fps`             |
| `xtim info`      | Show metadata about the experiment, hardware, and environment          | `xtim info --experiment exp123`                  |
| `xtim delete`    | Remove an experiment folder or logs                                    | `xtim delete logs`                               |
| `xtim test`      | Run scientific visual timing tests (e.g., flash perception)            | `xtim test --luminance`                          |

---

### 🔄 Common Workflows

#### 🔹 1. Creating and Running a New Experiment
```bash
xtim new
cd my_experiment/
xtim run
```

#### 🔹 2. Checking Device Availability
```bash
xtim devices list
xtim devices test --device pupil
```

#### 🔹 3. Validating Stimuli Assets
```bash
xtim assets validate
```

#### 🔹 4. Exporting Results
```bash
xtim export --output results.zip
```

#### 🔹 5. Archiving Completed Experiments
```bash
xtim archive my_experiment
```

#### 🔹 6. Debugging and Diagnostics
```bash
xtim doctor --fps
xtim doctor --luminance
```

#### 🔹 7. Launching the Interactive Menu
```bash
xtim menu
```

---

## 🔐 Data Ethics & Standards

XTIM aligns with:

- FAIR Data Principles
- Open Science guidelines
- GDPR and European data handling standards
- Institutional ethics frameworks (CSIC)

XTIM encourages reproducibility, transparency, and shareability.

---

## 📚 Academic References

- XSCAPE: Material Minds in Motion – CSIC-INCIPIT, 2023  
- OpenAIRE, FAIR data guidelines  
- Typer, Cookiecutter, LabStreamingLayer, Emobit, Pupil Labs SDK

---

## 👨‍🔬 Project Authors

Project developed by the **MaterialMindsLab** at INCIPIT-CSIC:

- **Arturo-José Valiño** – Lead Architect  
  arturo-jose.valino@incipit.csic.es

- **Rubén Álvarez-Mosquera** – Software Engineering  
  ruben.alvarez-mosquera@incipit.csic.es

---

## 📄 License

This software is released under the terms of the [EUROPEAN UNION PUBLIC LICENCE v. 1.2
EUPL © the European Union 2007, 2016](LICENSE.md).

---

## 🌐 Related Links

- [XSCAPE Official Portal](https://www.xscapeuos.com/)
- [INCIPIT-CSIC](https://www.incipit.csic.es)ç

---
© 2023–2025 CSIC-INCIPIT | XSCAPE-MaterialMinds Project | xtim development (MaterialMindsLab)
