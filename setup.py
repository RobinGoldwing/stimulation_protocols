# =============================================================================
# XTIM – Experimental Toolkit for Multimodal Neuroscience
# =============================================================================
# Part of the XSCAPE Project (Experimental Science for Cognitive and Perceptual Exploration)
#
# Developed by:
#   - Arturo-José Valiño
#   - Rubén Álvarez-Mosquera
#
# This software is designed to facilitate the creation, execution, and analysis
# of neuroscience experiments involving eye-tracking, EEG, and other modalities.
# It integrates with hardware and software tools such as Pupil Labs, Emobit,
# and MilliKey MH5, providing a unified command-line interface and interactive
# menu system for experiment management.
#
# For more information about the XSCAPE project, please refer to the project's
# documentation or contact the developers.
# =============================================================================

from setuptools import setup, find_packages

setup(
    name="xtim",
    version="0.1.0",
    description="Scientific experiment manager for EyeTracking, EEG, Emobit and stimuli",
    author="Tu Nombre o Grupo",
    author_email="tucorreo@ejemplo.com",
    packages=find_packages(),  # Encuentra todos los submódulos automáticamente
    include_package_data=True,
    install_requires=[
        "typer[all]",
        "cookiecutter",
        "pyyaml",
        "pylsl",
        "pandas",
        "numpy",
        "rich",
        "questionary",
        # Añadir aquí otros paquetes usados en el CLI o experimentos
    ],
    entry_points={
        "console_scripts": [
            "xtim = cli.main:app",  # Esto hace que puedas ejecutar `xtim` como comando
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
    ],
    python_requires=">=3.8",
)
