#!/bin/bash

# =============================================================================
# XTIM – Installation Script for Linux/macOS
# =============================================================================
# This script verifies the presence of Conda and initializes the XTIM
# experimental environment from ./config/conda-env/xtim-config-env.yml.
#
# Part of the XSCAPE Project
# Developed by Arturo-José Valiño and Rubén Álvarez-Mosquera
# =============================================================================

ENV_FILE="./config/conda-env/xtim-config-env.yml"
ENV_NAME="xtim-env"

echo "🔍 Checking system for Conda installation..."

if ! command -v conda &> /dev/null
then
    echo " Conda not found on this system."
    echo "Please install Miniconda from:"
    echo " https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

echo " Conda is available."

# Check if environment file exists
if [ ! -f "$ENV_FILE" ]; then
    echo " Environment file not found at $ENV_FILE"
    echo "Please ensure the file exists and try again."
    exit 1
fi

echo " Creating Conda environment '$ENV_NAME' from $ENV_FILE..."
conda env create -f "$ENV_FILE" || {
    echo " Environment creation failed. Check Conda logs for details."
    exit 1
}

echo " Environment '$ENV_NAME' created successfully."
echo " Installing xtim in editable mode..."
pip install -e . || {
    echo " Installation failed. Are you in the root of the xtim project?"
    echo "Try to execute: pip install -e . "
    exit 1
}
echo " xtim installed."

echo
echo " All done!"
echo " To begin, activate the environment with:"
echo "   conda activate $ENV_NAME"
echo " If 'xtim' is not recognized as a command, try running:"
echo "   python -m cli.main"
