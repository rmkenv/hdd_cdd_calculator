"""
HDD/CDD Calculator

A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD)
using weather data from multiple sources:

    - U.S. National Weather Service (NWS) API
    - Meteostat historical data API

The package allows:
    * Calculation of HDD/CDD for any location by latitude/longitude
    * Custom base temperature support
    * Source selection between NWS and Meteostat
    * Returning results as named tuples for easy processing
"""

# NWS data source
from .nws_api import (
    get_degree_days_for_location,
    get_degree_days_for_period,
    DegreeDaysResult,
)

# Meteostat data source
from .meteostat_api import fetch_meteostat_data

# Multi-source unified interface
from .data_sources import get_degree_days

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
    # NWS API
    "get_degree_days_for_location",
    "get_degree_days_for_period",

    # Meteostat API
    "fetch_meteostat_data",

    # Unified multi-source API
    "get_degree_days",

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
