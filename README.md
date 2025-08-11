# HDD/CDD Calculator

A Python library for calculating **Heating Degree Days (HDD)** and **Cooling Degree Days (CDD)** using weather data from the **U.S. National Weather Service (NWS) API**, with a modular design ready for additional weather data sources (e.g., Meteostat).

Heating and Cooling Degree Days are widely used in **energy demand prediction, HVAC planning, and climatology analysis**.  
This library provides an easy interface to retrieve forecast or historical temperature data and compute HDD/CDD.

[![PyPI version](https://img.shields.io/pypi/v/hdd-cdd-calculator.svg)](https://pypi.org/project/hdd-cdd-calculator/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## ✨ Features

- **Multiple data sources** – NWS API out-of-the-box, with design to add more (e.g., Meteostat).
- **Flexible calculations** – Any geographic location by latitude/longitude.
- **Custom base temperature** – Default 65°F, but easily changed.
- **Date range support** – Retrieve degree day data for specific periods.
- **Utility functions** – Coordinate validation, temperature conversions, mean temperature calculation.
- **Graceful error handling** – Custom exception classes for API and input errors.
- **Type hints** – For improved IDE support.
- **Unit tests included** – For core functionality.
- **PyPI-ready** – Easily installable.

---

## 📦 Installation

Install from PyPI:

```
pip install hdd-cdd-calculator
```

Or install from source:

```
git clone https://github.com/rmkenv/hdd_cdd_calculator.git
cd hdd_cdd_calculator
pip install .
```

---

## 🚀 Usage

### **Basic Usage**
Get HDD/CDD results for the White House coordinates (forecast data):

```
from hdd_cdd import get_degree_days_for_location

results = get_degree_days_for_location(38.8977, -77.0365)

for result in results:
    print(f"Date: {result.date}")
    print(f"High: {result.high_temp}°F, Low: {result.low_temp}°F")
    print(f"Mean: {result.mean_temp:.1f}°F")
    print(f"HDD: {result.hdd:.1f}, CDD: {result.cdd:.1f}")
    print()
```

---

### **Advanced Usage** – Specific Date Range

```
from hdd_cdd import get_degree_days_for_period

# Retrieve June 2023 data for New York City
results = get_degree_days_for_period(
    lat=40.7128,
    lon=-74.0060,
    start_date="2023-06-01",
    end_date="2023-06-30"
)

total_hdd = sum(r.hdd for r in results)
total_cdd = sum(r.cdd for r in results)

print(f"Total HDD: {total_hdd:.1f}")
print(f"Total CDD: {total_cdd:.1f}")
```

---

## 📖 API Reference

### **Functions**
#### `get_degree_days_for_location(lat, lon, base_temp=65.0)`
Fetches forecast data for the given coordinates and calculates HDD and CDD.

- **`lat`** *(float)* – Latitude (-90 to 90)
- **`lon`** *(float)* – Longitude (-180 to 180)
- **`base_temp`** *(float)* – Base temperature in °F (default: 65.0)
- **Returns** – List of `DegreeDaysResult` objects.

---

#### `get_degree_days_for_period(lat, lon, start_date, end_date, base_temp=65.0)`
Same as above, but filters results to the provided date range (inclusive).

- **`start_date`**, **`end_date`** – Strings in `YYYY-MM-DD` format.

---

#### `calculate_degree_days(high_temp, low_temp, base_temp=65.0)`
Utility function to calculate HDD/CDD given high/low temps.

---

### **Data Structures**
#### `DegreeDaysResult` *(NamedTuple)*
- `date` (str)
- `high_temp` (float)
- `low_temp` (float)
- `mean_temp` (float)
- `hdd` (float)
- `cdd` (float)

---

## ⚙ Development & Testing

Clone the repo and install dependencies:

```
git clone https://github.com/rmkenv/hdd_cdd_calculator.git
cd hdd_cdd_calculator
pip install -e .[dev]
```

Run the tests:

```
pytest
```

Format and lint code:

```
black .
flake8
mypy .
```

---

## 🤝 Contributing

1. Fork the repository.
2. Create your feature branch:  
   `git checkout -b feature/my-feature`
3. Commit your changes:  
   `git commit -m 'Add some feature'`
4. Push to the branch:  
   `git push origin feature/my-feature`
5. Open a pull request.

Contributions are welcome! Please ensure your code passes tests before submitting.

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 📚 Additional Project Files
- `pyproject.toml` — Build system configuration.
- `setup.py` / `setup.cfg` — Package configuration (for packaging to PyPI).
- `tests/` — Unit tests.
- `docs/` — Documentation.

---

**Author:** Ryan Kmetz  
📧 consultrmk@gmail.com

Repository: [GitHub – rmkenv/hdd_cdd_calculator](https://github.com/rmkenv/hdd_cdd_calculator)
PyPI: [hdd-cdd-calculator](https://pypi.org/project/hdd-cdd-calculator/)
```



If you’d like, I can also add a **section for future “Meteostat” integration** so contributors see that multi‑source support is planned.  
Do you want me to add that “Future Development” section?
