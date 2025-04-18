# {{ cookiecutter.experiment }}

> {{ cookiecutter.description }}

---
This experiment was generated using the **XTIM CLI system**, part of the XSCAPE Project (CSIC–INCIPIT).  
Template: `default/`  

## ✍️ Author and Metadata

| Field              | Value                                   |
|--------------------|-----------------------------------------|
| Author             | {{ cookiecutter.author_name }}          |
| Version            | {{ cookiecutter.version }}              |
| Contact            | {{ cookiecutter.author_email }}         |
| Version            | {{ cookiecutter.version }}              |
| Research area      | {{ cookiecutter.research_area }}        |
| Paradigm           | {{ cookiecutter.paradigm }}             |
| Ethics code        | {{ cookiecutter.ethics_code }}          |
| Language           | {{ cookiecutter.language }}             |
| Participant type   | {{ cookiecutter.participant_type }}     |

---

## 🧠 Devices Used

| Device             | Enabled |
|--------------------|---------|
| Pupil Labs Core    | {{ cookiecutter.use_pupil_core }} |
| Pupil Labs NEO     | {{ cookiecutter.use_pupil_neo }}  |
| EmotiBit           | {{ cookiecutter.use_emotibit }}   |
| EEG                | {{ cookiecutter.use_eeg }}        |
| MilliKey           | {{ cookiecutter.use_millikey }}   |
| LSL Synchronization| {{ cookiecutter.use_lsl }}        |

---

## 🎛️ Recording Configuration

| Parameter          | Value                  |
|--------------------|------------------------|
| Sampling Rate (Hz) | {{ cookiecutter.sampling_rate }} |
| Duration (min)     | {{ cookiecutter.duration_minutes }} |
| Segments           | {{ cookiecutter.segments }} |
| Calibration        | {{ cookiecutter.calibration }} |

---

## 🖥️ Display and Monitor

| Monitor Setting    | Value                    |
|--------------------|--------------------------|
| Resolution (px)    | {{ cookiecutter.resolution_x }} × {{ cookiecutter.resolution_y }} |
| Distance (cm)      | {{ cookiecutter.monitor_distance_cm }} |
| Width (cm)         | {{ cookiecutter.monitor_width_cm }} |
| Refresh Rate (Hz)  | {{ cookiecutter.monitor_refresh_hz }} |

| Display Parameter  | Value                    |
|--------------------|--------------------------|
| Background Color   | ({{ cookiecutter.bg_r }}, {{ cookiecutter.bg_g }}, {{ cookiecutter.bg_b }}) |
| Fullscreen         | {{ cookiecutter.fullscreen }} |
| Use GUI Window     | {{ cookiecutter.use_gui }} |
| Screen Index       | {{ cookiecutter.screen_index }} |
| Color Space        | {{ cookiecutter.color_space }} |
| Flip Interval      | {{ cookiecutter.flip_interval_override }} |

---

## 🔗 Synchronization

| Sync Method        | {{ cookiecutter.sync_method }} |
|--------------------|--------------------------------|
{% if cookiecutter.sync_method == 'ttl' %}
| TTL Port           | {{ cookiecutter.ttl_port }} |
{% elif cookiecutter.sync_method == 'lsl' %}
| LSL Stream Name    | {{ cookiecutter.lsl_stream_name }} |
{% endif %}

---

## 📁 Folder Structure

- `__data__/`: Raw experiment data  
- `__models__/`: Models  
- `__notebooks__/`: Jupyter Notebooks  
- `__results__/`: Results data  
- `__output__/`: Processed or derived outputs  
- `log/`: Execution and debug logs  
- `scripts/`: Stimulus control scripts  
- `config/`: All configuration files (TOML, YAML)  

---


# 🧾 Notes

## xtim – Experimental Framework for Multimodal Neurocognitive Research

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
