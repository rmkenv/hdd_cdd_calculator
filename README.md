# HDD/CDD Calculator

[![PyPI version](https://img.shields.io/p://pypi.org/project/hdd-cdd versions](https://img.shields.io/pypi/pyversions/h://pypi.org/project/hdd-cdd library for calculating **Heating Degree Days (HDD)** and **Cooling Degree Days (CDD)** from multiple weather data sources, including:

- **U.S. National Weather Service (NWS) API** — forecast data  
- **Meteostat** — global historical weather data

This package and repository are designed primarily for **energy managers and sustainability professionals in the United States** who need to:

- Understand how outdoor weather influences **energy efficiency**  
- **Forecast** energy usage based on HDD/CDD trends  
- Integrate weather-normalized analysis into energy reporting, benchmarking, and decision-making

It’s suitable for both quick exploratory analyses and production workflows.

The package also supports:
- Automated alignment of energy usage CSV data with degree days
- Linear regression analysis between degree days and energy consumption
- Visualization of regression results
- An **included example dataset** for quick testing
- A **CLI** to run the full workflow and save the plot

***

## ⚠️ Important Notes on Data Quality & Limitations

For energy efficiency analysis and forecasting, the quality of your weather data matters. Be aware of:

- **Missing or Low-Quality In Situ Data**  
  Some station datasets may have missing data or poor quality control (QC). Meteostat does not apply extensive QC, and gaps or extreme values can bias results.

- **Limitations of Gridded Weather Data**  
  Reanalysis datasets (e.g., ERA5) are not always direct substitutes for local station observations and can be biased in some regions, especially the tropics.

Understanding these factors helps you choose the right source and interpret results realistically.

For a deeper discussion of these issues in engineering contexts, see:  
*“On the Use of Observed and Gridded Weather Data in Energy Analysis” — ESS Open Archive*  
[https://essopenarchive.org/doi/full/10.22541/essoar.175130623.32640121/v1](https://essopenarchive.org/doi/full/10.22541/essoar.175130623.32640121/v1)

***

## ✨ Features

- U.S.-focused but works with global locations (via Meteostat)
- Calculate HDD/CDD for any lat/lon with custom base temperature
- Retrieve data for date ranges
- Two sources: NWS (U.S. forecast) & Meteostat (global historical)
- CSV utilities for loading & aligning energy consumption
- Linear regression between HDD/CDD and energy usage
- Matplotlib visualizations
- Example dataset & CLI for end-to-end run
- Clear error handling & type hints  
- PyPI-ready packaging

***

## 📦 Installation

From PyPI:
```bash
pip install hdd-cdd-calculator
```

Optional extras:
```bash
pip install hdd-cdd-calculator[dev]   # development tools
pip install hdd-cdd-calculator[viz]   # plotting support
```

From source:
```bash
git clone https://github.com/rmkenv/hdd_cdd_calculator.git
cd hdd_cdd_calculator
pip install -e .[dev]
```

***

## 🚀 Basic Usage

These examples assume **U.S.-based energy managers or sustainability teams** who want to evaluate weather-normalized performance.

### NWS Data Source
```python
from hdd_cdd_calculator import get_degree_days

results = get_degree_days(
    lat=38.8977,
    lon=-77.0365,
    start_date="2023-06-01",
    end_date="2023-06-07",
    source="nws"
)
```

### Meteostat Data Source
```python
from hdd_cdd_calculator import get_degree_days

results = get_degree_days(
    lat=40.7128,
    lon=-74.0060,
    start_date="2023-06-01",
    end_date="2023-06-30",
    source="meteostat"
)
```

***

## 📂 Working with Energy CSVs

Energy managers can align internal usage data with HDD/CDD for regression and forecasting.

Expected CSV headers:
```
date,kwh,mmbtu,gal
```

Example — regression workflow:
```python
from hdd_cdd_calculator import (
    get_degree_days_for_period,
    align_energy_with_degree_days,
    perform_regression,
    plot_regression
)
```

***

## ⚡ Quick Try (U.S. Example Dataset)

Perfect for testing the workflow end-to-end for energy efficiency analysis.

```bash
python -m hdd_cdd_calculator --example
```

Runs a **NYC June 2023** HDD correlation against sample building energy data.

***

## 📖 API Overview
*(unchanged list of functions)*

***

## 🧪 Development

```bash
git clone https://github.com/rmkenv/hdd_cdd_calculator.git
cd hdd_cdd_calculator
pip install -e .[dev]
pytest
```

***

## 🔍 Use Cases
This package is particularly useful for energy managers and sustainability professionals to:

- Perform weather-normalized evaluation of building energy consumption

- Forecast heating and cooling energy demands based on degree day trends

- Support energy efficiency reporting and benchmarking initiatives

- Identify changes in energy performance relative to outdoor temperature variations

- Integrate degree day analysis into sustainability goals and compliance tracking

- Model energy consumption sensitivity to temperature fluctuations for operational planning

These use cases leverage the HDD/CDD calculations and regression tools to give actionable insights into how weather impacts energy usage and efficiency.

***

## 📜 License

MIT License — see [LICENSE](LICENSE).  
**Author:** Ryan Kmetz

***

