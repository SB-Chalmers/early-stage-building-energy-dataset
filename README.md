# Early-stage Building Energy Dataset

[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.egyai.2025.100557-blue)](https://doi.org/10.1016/j.egyai.2025.100557) [![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

This repository contains materials for my PhD research on creating machine learning models to predict residential building energy demand from early-stage architectural design variables.

## Research focus

The PhD project investigates how simple architectural design variables (shape, orientation, glazing ratio, building compactness, etc.) influence annual energy demand. The goal is to produce fast, accurate surrogate models that can be used during early design exploration to estimate heating and cooling loads without running costly simulations.

## Included datasets and artifacts

1. Grasshopper generation script  that produces 9 building shapes with different architectural design variables. See `data/grasshopper/`.
2. Synthetic training data mapping individual architectural design variables to their respective yearly energy demand. See `data/synthetic/data_all_adv.csv`and `data/synthetic/README.md` for details.
3. Developed machine learning models. See `models/`.

## Repository structure

The repository is organized for clarity and reproducibility:

- `data/`
  - `grasshopper/` - Grasshopper scripts to generate the 9 building shapes.
  - `synthetic/` - Synthetic training datasets (CSV files). 
- `models/` - Trained model artifacts and model metadata. 
- `docs/` - Usage instructions, methodology notes, and how to reproduce results.
- `requirements.txt` - Python dependencies for training and inference.
- `.gitignore` - Common ignores for models, virtual environments, and datasets.

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment (PowerShell):

   PS> python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1

2. Install dependencies:

   PS> pip install -r requirements.txt



Citation
--------
If you use this dataset or code in your research, please cite the peer-reviewed paper associated with this project:

https://doi.org/10.1016/j.egyai.2025.100557


