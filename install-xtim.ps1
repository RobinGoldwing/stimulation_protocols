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

Write-Host "🔍 Checking system for Conda installation..."

$conda = Get-Command conda -ErrorAction SilentlyContinue
if (-not $conda) {
    Write-Host "❌ Conda not found on this system."
    Write-Host "Please install Conda/Miniconda from:"
    Write-Host "👉 https://docs.conda.io/"
    exit 1
}

Write-Host "✅ Conda is available."

if (-Not (Test-Path $envFile)) {
    Write-Host "❌ Environment file not found at $envFile"
    Write-Host "Please ensure the file exists and try again."
    exit 1
}

Write-Host "📦 Creating Conda environment '$envName' from $envFile..."
conda env create -f "$envFile"

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️ Environment creation failed. Check Conda logs for details."
    exit 1
}

Write-Host "✅ Environment '$envName' created successfully."
Write-Host "ℹ️ You may now activate it using:"
Write-Host "   conda activate $envName"
