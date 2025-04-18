<#
===============================================================================
XTIM – Installation Script for Windows (PowerShell)
===============================================================================
This script verifies the presence of Conda and initializes the XTIM
experimental environment from ./config/conda-env/xtim-config-env.yml.

Part of the XSCAPE Project
Developed by Arturo-José Valiño and Rubén Álvarez-Mosquera
===============================================================================
#>

$envFile = ".\config\conda-env\xtim-config-env.yml"
$envName = "xtim-env"

Write-Host 'Checking system for Conda installation...'

$conda = Get-Command conda -ErrorAction SilentlyContinue
if (-not $conda) {
Write-Host 'Conda not found on this system.'
Write-Host 'Please install Conda/Miniconda from:'
Write-Host 'https://docs.conda.io/'
    exit 1
}

Write-Host 'Conda is available.'

if (-Not (Test-Path $envFile)) {
Write-Host 'Environment file not found at $envFile'
Write-Host 'Please ensure the file exists and try again.'
    exit 1
}

Write-Host 'Creating Conda environment '$envName' from '$envFile'...'
conda env create -f "$envFile"
if ($LASTEXITCODE -ne 0) {
Write-Host 'Environment creation failed.'
Write-Host 'Try to execute: conda env create -f '$envFile' '
    exit 1
}

Write-Host 'Environment '$envName' created successfully.'

# Try to activate the environment
Write-Host "Attempting to activate environment '$envName'..."

try {
    conda activate $envName
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Environment '$envName' activated successfully."
    } else {
        Write-Warning "Activation failed. You may need to run 'conda init' or restart your terminal."
        Write-Host "You can manually activate it with: conda activate $envName"
    }
} catch {
    Write-Warning "Error during activation: $_"
    Write-Host "You can manually activate the environment with: conda activate $envName"
}


Write-Host 'Installing xtim in editable mode...'
pip install -e .
if ($LASTEXITCODE -ne 0) {
Write-Host 'pip install failed. Are you in the project root?'
Write-Host 'Try to execute: pip install -e .'
    exit 1
}


Write-Host 'Testing xtim help command: < xtim --help >'
xtim doctor status

Write-Host 'Testing xtim help command: < xtim --help >'
xtim --help

Write-Host ''
Write-Host 'Installation complete!'
Write-Host 'To begin, activate the environment:'
Write-Host 'conda activate xtim-env'
Write-Host 'If 'xtim' command is not found, try:'
Write-Host 'python -m cli.main'