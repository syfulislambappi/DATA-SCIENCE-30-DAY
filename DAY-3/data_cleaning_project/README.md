# Data Cleaning Project - Client Delivery Template

This repository is a professional, client-ready data cleaning template using **pandas**.
It includes a sample messy dataset, a notebook with visualizations, reusable scripts, and export-ready CSV output.

## Structure
- `data/` - contains sample raw and cleaned data
  - `messy_customers.csv` - example input with common issues
- `notebooks/` - Jupyter notebooks
  - `client_data_cleaning_with_visuals.ipynb` - the main client-facing notebook (with charts)
- `scripts/` - reusable Python modules for running the cleaning pipeline
  - `cleaning_pipeline.py`
  - `utils.py`
- `README.md` - this file

## How to use
1. Replace `data/messy_customers.csv` with your client's raw CSV (keep a copy of raw data).
2. Open `notebooks/client_data_cleaning_with_visuals.ipynb` and run cells top-to-bottom.
3. Review the "Initial profiling" section and customize lists (numeric/date columns) as needed.
4. After running, the cleaned dataset will be saved to `data/cleaned_customers.csv`.

## Customization checklist (before delivering to client)
- [ ] Update dataset path and file names
- [ ] Customize numeric & date column lists in notebook and scripts
- [ ] Add domain-specific validation rules (e.g., age limits, country codes)
- [ ] Document all major decisions in the notebook (changelog cell)
- [ ] Add unit tests or quick validation assertions if required by client

## Deliverables for client
- Cleaned CSV (`data/cleaned_customers.csv`)
- `client_data_cleaning_with_visuals.ipynb` for reproducibility and audit
- `cleaning_pipeline.py` for integration into ETL

