# 🛠️ INSTALL.md – XTIM Installation Guide

This document provides detailed instructions for installing and initializing the XTIM experimental toolkit in a research environment.

---

## 📦 Requirements

Before starting, ensure your system has the following:

- Python 3.8 or higher (recommended: via Anaconda)
- Git (for cloning the repository)
- Conda (Miniconda or Anaconda)
- pip (Python package manager)

---

## ⏬ 1. Clone the Repository

Clone the latest version of the XTIM system:

```bash
git clone https://github.com/your-org/xtim.git
cd xtim
```

If you are installing from a ZIP file, extract it and enter the directory:

```bash
unzip xtim.zip
cd xtim
```

---

## 🧪 2. Create Conda Environment

Create a new Conda environment with all scientific dependencies:

```bash
conda env create -f config/conda-env/xtim-config-env.yml
```

Then activate it:

```bash
conda activate xtim
```

Check Python version:

```bash
python --version
```

---

## 📥 3. Install XTIM Locally

Use the editable install method so you can modify the code live:

```bash
pip install -e .
```

This allows the `xtim` command to be available globally in your terminal.

---

## 🔄 Optional: Use Provided Install Scripts

For convenience, installation scripts are available:

- For Linux/macOS:
  ```bash
  bash install-xtim.sh
  ```

- For Windows (PowerShell):
  ```powershell
  ./install-xtim.ps1
  ```

These scripts wrap the above steps and auto-detect platform specifics.

---

## ✅ 4. Test the Installation

Run a quick check:

```bash
xtim doctor
```

This should perform system diagnostics, check FPS, available modules, and supported commands.

---

## 📚 What’s Next?

You’re ready to:

- Create your first experiment with `xtim new`
- Explore command-line tools with `xtim --help`
- Read additional docs like `RUNNING_EXPERIMENTS.md` or `COMMANDS_USAGE.md`

---

## 📂 Recommended Folder Structure

We recommend placing the repository inside a general workspace directory:

```
~/research-lab/
└── xtim/                 ← cloned here
    ├── experiments/
    ├── config/
    └── ...
```

---

## 🧠 Pro Tips

- Always activate your environment before running XTIM:
  ```bash
  conda activate xtim
  ```
- Use version control (`git`) for your own experiments.
- Maintain a virtual environment per project if needed.
- Customize the `xtim` CLI using the modular `cli/` folder.

---

## ❓ Troubleshooting

- Conda not found? Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- XTIM not found after install? Try restarting terminal or check `$PATH`
- Still issues? Run:
  ```bash
  pip uninstall xtim
  pip install -e .
  ```

---

## 👨‍🔬 Maintainers

For help, contact the project leads:

- Arturo-José Valiño – arturo-jose.valino@incipit.csic.es
- Rubén Álvarez-Mosquera – ruben.alvarez-mosquera@incipit.csic.es

---
