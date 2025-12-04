# Early-stage Building Energy Dataset

[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.egyai.2025.100557-blue)](https://doi.org/10.1016/j.egyai.2025.100557) [![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

This repository contains materials for my PhD research on creating machine learning models to predict residential building energy demand from early-stage architectural design variables.

## Research focus

The PhD project investigates how simple architectural design variables (shape, orientation, glazing ratio, building compactness, etc.) influence annual energy demand. The goal is to produce fast, accurate surrogate models that can be used during early design exploration to estimate heating and cooling loads without running costly simulations.

## Included datasets and artifacts

1. Grasshopper generation script (or instructions) that produces 9 building shapes with different architectural design variables. See `data/grasshopper/`.
2. Synthetic training data mapping individual architectural design variables to their respective yearly energy demand. See `data/synthetic/sample_synthetic.csv` for a small example and `data/synthetic/README.md` for details.
3. Developed machine learning models and example training code. See `models/` and `scripts/train_model.py`.

## Repository structure

The repository is organized for clarity and reproducibility:

- `data/`
  - `grasshopper/` - Grasshopper script(s) or instructions to generate the 9 building shapes.
  - `synthetic/` - Synthetic training datasets (CSV files). A small sample is included for quick tests.
- `models/` - Trained model artifacts and model metadata. (Contains a README and example saved models.)
- `scripts/` - Python scripts to train models, run predictions, and preprocess data.
- `docs/` - Usage instructions, methodology notes, and how to reproduce results.
- `requirements.txt` - Python dependencies for training and inference.
- `.gitignore` - Common ignores for models, virtual environments, and datasets.

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment (PowerShell):

   PS> python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1

2. Install dependencies:

   PS> pip install -r requirements.txt

3. Train a quick example model using the included sample dataset:

   PS> python .\\scripts\\train_model.py --data .\\data\\synthetic\\sample_synthetic.csv --output models/rf_model.joblib

4. See `docs/USAGE.md` for more details, including how to run inference and add your own Grasshopper outputs.

## Notes

- The included `sample_synthetic.csv` is a small, synthetic example for development and testing only. It is not representative of real-world energy use.
- For production experiments, replace the sample CSV with your full synthetic dataset in `data/synthetic/` and consider storing large datasets outside the repository (e.g., a data server or cloud storage).

If you'd like, I can also add example notebooks, evaluation scripts, or CI to run unit tests on the training pipeline.

Citation
--------
If you use this dataset or code in your research, please cite the peer-reviewed paper associated with this project:

https://doi.org/10.1016/j.egyai.2025.100557


