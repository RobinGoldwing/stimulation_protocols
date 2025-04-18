#!/bin/bash

###############################################################################
# XTIM – Installation Script for Linux/macOS
###############################################################################
# This script initializes the Conda environment for the XTIM system
# and installs xtim in editable mode.
#
# Part of the XSCAPE Project | INCIPIT-CSIC
###############################################################################

ENV_FILE="./config/conda-env/xtim-config-env.yml"
ENV_NAME="xtim-env"

fail_exit() {
    echo ""
    echo "ERROR: $1"
    exit 1
}

echo ""
echo "Checking system for Conda..."

if ! command -v conda &> /dev/null; then
    fail_exit "Conda not found. Please install Miniconda from https://docs.conda.io/"
fi

echo "Conda is available."

if [ ! -f "$ENV_FILE" ]; then
    fail_exit "Environment file not found at $ENV_FILE"
fi

echo ""
echo "Creating environment '$ENV_NAME' from '$ENV_FILE'..."
conda env create -f "$ENV_FILE"
if [ $? -ne 0 ]; then
    fail_exit "Environment creation failed. Try: conda env create -f $ENV_FILE"
fi

echo "Environment '$ENV_NAME' created."


echo ""
echo "Installing xtim in editable mode..."
pip install -e .
if [ $? -ne 0 ]; then
    fail_exit "pip install failed. Make sure you're in the root of the xtim project."
fi

echo "xtim installed."

echo ""
echo "Verifying installation..."
xtim doctor status
xtim --help

echo ""
echo "Installation complete and validated."
echo ""
echo "Please activate the environment manually:"
echo "   conda activate $ENV_NAME"
