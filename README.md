# HDD/CDD Calculator

A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD) using weather data from the National Weather Service (NWS) API. https://pypi.org/project/hdd-cdd-calculator/

---

## Features

- Calculate HDD and CDD for any geographic location by latitude and longitude.
- Support for custom base temperatures.
- Retrieve degree day data for specific date ranges.
- Graceful handling of errors and invalid inputs.
- Type hints for improved code clarity and IDE support.
- Unit tests included for core functionality.
- Ready for packaging and distribution via PyPI.

---

## Installation

Install the package via pip:

```bash
pip install hdd-cdd-calculator

Usage
Basic Usage
from hdd_cdd import get_degree_days_for_location

# Get degree days for a specific location (e.g., White House coordinates)
results = get_degree_days_for_location(38.8977, -77.0365)

for result in results:
    print(f"Date: {result.date}")
    print(f"High: {result.high_temp}°F, Low: {result.low_temp}°F")
    print(f"Mean: {result.mean_temp:.1f}°F")
    print(f"HDD: {result.hdd:.1f}, CDD: {result.cdd:.1f}")
    print()

Advanced Usage with Date Range
from hdd_cdd import get_degree_days_for_period

# Get degree days for New York City for June 2023
results = get_degree_days_for_period(
    lat=40.7128,
    lon=-74.0060,
    start_date="2023-06-01",
    end_date="2023-06-30"
)

total_hdd = sum(result.hdd for result in results)
total_cdd = sum(result.cdd for result in results)

print(f"Total HDD for June 2023: {total_hdd:.1f}")
print(f"Total CDD for June 2023: {total_cdd:.1f}")

Documentation

Full documentation is available in the docs directory.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Additional Project Files
pyproject.toml — Build system configuration.
setup.cfg — Package metadata and configuration.
.gitignore — Recommended ignores for Python projects, including build artifacts, virtual environments, and IDE files.

If you have any questions or want to contribute, feel free to open an issue or submit a pull request!


