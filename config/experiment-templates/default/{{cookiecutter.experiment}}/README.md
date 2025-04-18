# {{ cookiecutter.experiment }}

**Author**: {{ cookiecutter.author_name }}  
**Description**: {{ cookiecutter.description }}  
**Version**: {{ cookiecutter.version }}  
**Created**: {{ cookiecutter._template_context_cookiecutter.creation_date | default('2025-04-18') }}

---

## 🧠 Devices

| Device        | Enabled |
|---------------|---------|
| Pupil Labs Core | {{ cookiecutter.use_pupil_core }} |
| Pupil Labs NEO  | {{ cookiecutter.use_pupil_neo }} |
| EmotiBit        | {{ cookiecutter.use_emotibit }} |
| EEG             | {{ cookiecutter.use_eeg }} |
| MilliKey        | {{ cookiecutter.use_millikey }} |

---

## 🎛️ Recording

- **Duration**: {{ cookiecutter.duration_minutes }} minutes  
- **Sampling Rate**: {{ cookiecutter.sampling_rate }} Hz

---

## 📁 Structure

- `data/`: Raw experiment data  
- `log/`: Log files and runtime information  
- `scripts/`: Stimulus scripts  
- `config/`: Configuration files  
- `objects-output/`: Exported derived data

---

## 🔖 Notes

This experiment was generated using the **XTIM framework** as part of the XSCAPE project (INCIPIT/CSIC).
