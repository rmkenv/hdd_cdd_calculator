"""
HDD/CDD Calculator

A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD)
using multiple weather data sources such as:

    - U.S. National Weather Service (NWS) API
    - Meteostat historical data API

The package also includes:
    * Utilities for coordinate validation, temperature conversions, and HDD/CDD calculations
    * Unified API for selecting a data source
    * Linear regression analysis between degree days and energy consumption
"""

# NWS data source
from .nws_api import (
    get_degree_days_for_location,
    get_degree_days_for_period,
    DegreeDaysResult,
)

# Meteostat data source
from .meteostat_api import fetch_meteostat_data

# Unified multi-source access
from .data_sources import get_degree_days

# Regression analysis
from .regression import perform_regression

# Utilities
from .utils import (
    validate_coordinates,
    calculate_degree_days,
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
    mean_temperature,
)

# Exceptions
from .exceptions import (
    NWSAPIError,
    InvalidCoordinatesError,
)

__version__ = "0.1.3"

__all__ = [
    # Core NWS API
    "get_degree_days_for_location",
    "get_degree_days_for_period",

    # Meteostat API
    "fetch_meteostat_data",

    # Unified multi-source
    "get_degree_days",

    # Regression analysis
    "perform_regression",

    # Data structures
    "DegreeDaysResult",

    # Utilities
    "validate_coordinates",
    "calculate_degree_days",
    "fahrenheit_to_celsius",
    "celsius_to_fahrenheit",
    "mean_temperature",

    # Exceptions
    "NWSAPIError",
    "InvalidCoordinatesError",
]
