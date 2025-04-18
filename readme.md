
# xtim – Experimental Framework for Multimodal Neurocognitive Research

**xtim** is used for presenting stimuli of the [XSCAPE Project](https://www.incipit.csic.es/en/project/xscape) at CSIC-INCIPIT.  
It is designed to support **human cognition research** across eye-tracking, physiology, behavior and brain activity.

📚 For literature and references on the XSCAPE framework, see:
- XSCAPE: Material Minds in Motion – Project Description (CSIC-INCIPIT, 2023)
- All XSCAPE-related info at: [https://www.xscapeuos.com/]

## Status

🛠️ **Under Development**  
This code is currently a work in progress. The code for running experiments synchronizing eye trakcin/emotibit is already up and working.

For contributions, feedback, and suggestions are very welcome, contact the corresponding author.


👨‍💻 **Developers - MaterialMindsLab**: 

Arturo-Jose Valiño (Lead) : arturo-jose.valino@incipit.csic.es

Rubén Álvarez-Mosquera (Dev) : ruben.alvarez-mosquera@incipit.csic.es

---

## 🧭 Features

It supports multimodal data acquisition using:

- 🧠 **Pupil Labs Core/Neo** eye-tracking
- 💓 **EmotiBit** physiological bands (EDA, BVP, accelerometry…)
- 🌐 **LSL** (Lab Streaming Layer) for real-time data synchronization
- ⚡ **EEG** systems (future integration)


- CLI-driven experiment creation using Cookiecutter templates
- Multimodal acquisition: Pupil Labs (Core/Neo), EmotiBit, EEG (future)
- Real-time LSL integration for cross-device synchronization
- Structured experiment folders with config, scripts, data, logs
- TOML-based metadata for reproducibility and FAIR alignment
- Export & inspection tools for documentation and publication
- Conda environment templates per hardware modality

---

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/Rockyneuron/stimulation_protocols
cd stimulation_protocols
pip install -e .

# List available experiment templates
xtim new list

# Create a new experiment from a template
xtim new experiment default -o LABORATORY/

# Run an experiment
xtim run --path LABORATORY/example_experiment/
```

---

## 🧠 Why `xtim`?

- Built for real-time, multimodal, embodied cognition studies
- Adaptable to lab and field studies
- Open, modular, metadata-aware
- Bridges stimuli, acquisition and reproducibility

---

## 📄 License

EUROPEAN UNION PUBLIC LICENCE v. 1.2
EUPL © the European Union 2007, 2016

---
© 2023–2025 CSIC-INCIPIT | XSCAPE-MaterialMinds Project | xtim development (MaterialMindsLab)
