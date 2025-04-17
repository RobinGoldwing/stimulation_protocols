# Lab Name : {{ cookiecutter.lab_name }}

Description: {{ cookiecutter.description }}

Author: {{ cookiecutter.author }}

---

## 🧪 Environment Setup

This lab uses [Poetry](https://python-poetry.org/) to manage dependencies.

### 1. Install Poetry (if not installed)

Follow the instructions at: https://python-poetry.org/docs/#installation

### 2. Initialize the environment

```bash
./init.sh
```

This will:
- Install dependencies from `pyproject.toml`
- Register the lab as a Jupyter kernel (named after this lab)

---

## 📓 Recommended Structure

```
{{ cookiecutter.lab_name }}/
├── notebooks/           ← Jupyter notebooks
├── data/                ← Input and output data
├── experiments/         ← Code or scripts for each experiment
├── env/                 ← Environments
├── pyproject.toml       ← Poetry environment definition
├── init.sh              ← Setup script for the lab
└── README.md            ← This file
```

---

## 🧠 Tips

- Use `poetry shell` to enter the virtual environment manually
- Launch JupyterLab using the registered kernel:
  ```bash
  jupyter lab
  ```

Enjoy your reproducible scientific environment!
