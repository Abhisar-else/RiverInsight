# RiverInsight — Geospatial ML for River Water Quality

An independent portfolio project inspired by the water-quality prediction problem explored in the 2026 EY AI & Data Challenge. This repository is **not an official EY submission** and does not imply EY endorsement or participation.

## Project goal
Build a reproducible pipeline to explore and, where suitable labeled data is legally available, predict:
- Total alkalinity (TA)
- Electrical conductance (EC)
- Dissolved reactive phosphorus (DRP)

Potential predictors include sample date, coordinates, climate, terrain, and satellite-derived features.

## Project status
**Phase 1: research and data audit.** No model results are claimed yet.

## Responsible research rules
- Check access and license terms before downloading or redistributing data.
- Do not commit restricted challenge files, secrets, or large raw datasets.
- Keep a record of source URLs, access dates, licenses, units, and transformations.
- Do not treat below-detection-limit measurements as zero without scientific justification.
- Evaluate geographic generalization; random splits alone may be misleading.
- Report actual metrics only, with the split strategy and limitations.

## Planned phases
1. Research and data audit
2. Repository and data pipeline
3. Exploratory data analysis
4. Baseline and ML models
5. Geospatial features and spatial validation
6. Reliability and explainability
7. Reproducible training/inference workflow
8. Dashboard, report, and resume

## Hardware-conscious approach
Start with small CSV files and CPU-friendly models. Do not download complete satellite archives until a small pilot proves the workflow works.

## Setup
Use Python 3.11+ in a virtual environment. Install the dependencies listed in `requirements.txt`.

## Repository layout
- `data/`: local data only; raw data is git-ignored
- `notebooks/`: exploratory analysis
- `src/`: reusable pipeline code
- `tests/`: validation tests
- `reports/`: notes, evaluation results, and project report
