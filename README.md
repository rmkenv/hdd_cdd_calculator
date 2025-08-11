# HDD/CDD Calculator

[![Update Example Plot](https://github.com/rmkenv/hdd_cdd_calculator/actions/workflows/update-example-plot.yml/badge.svg)](https://github.com/rmkenv/hdd_cdd_calculator/actions/workflows/update-example-plot.yml)
[![PyPI version](https://img.shields.io/pypi/v/hdd-cdd-calculator)](https://pypi.org/project/hdd-cdd-calculator/)
[![Python versions](https://img.shields.io/pypi/pyversions/hdd-cdd-calculator)](https://pypi.org/project/hdd-cdd-calculator/)

A Python library for calculating **Heating Degree Days (HDD)** and **Cooling Degree Days (CDD)** from multiple weather data sources, including:

- **U.S. National Weather Service (NWS) API** – forecast data  
- **Meteostat** – global historical weather data

The package also supports:
- Automated alignment of energy usage CSV data with degree days
- Linear regression analysis between degree days and energy consumption
- Visualization of regression results
- An **included example dataset** for quick testing
- A simple **CLI** to run the full workflow and save the plot

---

## ✨ Features

- Calculate HDD/CDD for any location by latitude/longitude
- Custom base temperature support
- Retrieve degree day data for specific date ranges
- **Two data sources**: NWS (U.S. forecast) and Meteostat (global historical)
- CSV utilities for loading and aligning energy consumption data
- **Linear regression** between degree days and energy usage
- **Matplotlib visualization** of results
- CLI example that runs end-to-end and saves a screenshot
- Clear error handling and type hints
- PyPI-ready packaging

---

## 📦 Installation

From PyPI:
```
pip install hdd-cdd-calculator
```

Optional extras:
```
pip install hdd-cdd-calculator[dev]   # dev tools (pytest, linting, typing)
pip install hdd-cdd-calculator[viz]   # includes matplotlib for plotting
```

From source:
```
git clone https://github.com/rmkenv/hdd_cdd_calculator.git
cd hdd_cdd_calculator
pip install -e .[dev]
```

---

## 🚀 Basic Usage

### NWS Data Source
```
from hdd_cdd_calculator import get_degree_days

results = get_degree_days(
    lat=38.8977,
    lon=-77.0365,
    start_date="2023-06-01",
    end_date="2023-06-07",
    source="nws"
)

for r in results:
    print(f"{r.date} | High: {r.high_temp}°F | Low: {r.low_temp}°F | HDD: {r.hdd} | CDD: {r.cdd}")
```

### Meteostat Data Source
```
from hdd_cdd_calculator import get_degree_days

results = get_degree_days(
    lat=40.7128,
    lon=-74.0060,
    start_date="2023-06-01",
    end_date="2023-06-30",
    source="meteostat"
)
```

---

## 📂 Working with Energy CSVs

Expected CSV headers:
```
date,kwh,mmbtu,gal
```

### Load Energy Data
```
from hdd_cdd_calculator import read_energy_data_from_csv
energy_values = read_energy_data_from_csv("energy_data.csv", column="kwh")
```

### Align CSV & Degree Days → Regression → Plot
```
from hdd_cdd_calculator import (
    get_degree_days_for_period,
    align_energy_with_degree_days,
    perform_regression,
    plot_regression
)
import pandas as pd

# Step 1: Fetch HDD data
dd_results = get_degree_days_for_period(
    lat=40.7128,
    lon=-74.0060,
    start_date="2023-06-01",
    end_date="2023-06-10"
)

# Step 2: Align with CSV
energy_vals, hdd_vals = align_energy_with_degree_days(
    dd_results,
    "examples/sample_energy_data.csv",
    energy_column="kwh",
    degree_day_type="hdd"
)

# Step 3: Fit regression
model = perform_regression(hdd_vals, energy_vals)
print(f"Slope: {model.coef_:.2f}, Intercept: {model.intercept_:.2f}")

# Step 4: Plot and save
plot_regression(
    pd.Series(hdd_vals),
    pd.Series(energy_vals),
    model,
    save_path="examples/regression_plot.png"  # Save file in examples/
)
```

---

## ⚡ Quick Try (With Included Dataset)

We include a complete dataset + CLI workflow.

From the repo root or after installing:
```
python -m hdd_cdd_calculator --example
```

This will:
1. Fetch HDD data for NYC (June 1–10, 2023)  
2. Align with `examples/sample_energy_data.csv`  
3. Perform regression  
4. Display a plot and save it to `examples/regression_plot.png`

### Example Output
![Regression Example](examples/regression_plot.png)

---

## 📖 API Overview

**Data fetching**
- `get_degree_days_for_location(...)`
- `get_degree_days_for_period(...)`
- `fetch_meteostat_data(...)`
- `get_degree_days(...)` — unified source selector

**CSV utilities**
- `read_energy_data_from_csv(path, column="kwh")`
- `read_energy_data_with_dates(path, column="kwh")`
- `align_energy_with_degree_days(degree_days, csv, energy_column="kwh", degree_day_type="hdd")`

**Analysis**
- `perform_regression(degree_days, energy_usage)`
- `plot_regression(degree_days, energy_usage, model, save_path=None, show=True)`

**Utilities**
- `validate_coordinates(...)`
- `calculate_degree_days(...)`
- Temperature conversions: `fahrenheit_to_celsius(...)`, `celsius_to_fahrenheit(...)`

---

## 🧪 Development

Clone and install with developer tools:
```
git clone https://github.com/rmkenv/hdd_cdd_calculator.git
cd hdd_cdd_calculator
pip install -e .[dev]
```

Run tests:
```
pytest
```

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

**Author:** Ryan Kmetz
```

