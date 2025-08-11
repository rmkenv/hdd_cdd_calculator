"""
A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD).

Currently supports fetching forecast temperature data from the U.S. National Weather Service (NWS) API
to compute HDD/CDD values. The design is modular so additional weather data providers (e.g., Meteostat)
can be integrated easily.

Public API:
  - Degree day calculations from daily high/low temperatures
  - Retrieve HDD/CDD for a single location or a date range
  - Utility functions for coordinate validation and temperature conversions
"""

from .calculator import (
    DegreeDaysResult,
    get_degree_days_for_location,
    get_degree_days_for_period,
)
from .exceptions import InvalidCoordinatesError, NWSAPIError
from .meteostat_api import fetch_meteostat_data
from .utils import (
    calculate_degree_days,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    mean_temperature,
    validate_coordinates,
)

__version__ = "0.1.3"

__all__ = [
    # Core calculation entry points
    "calculate_degree_days",
    "get_degree_days_for_location",
    "get_degree_days_for_period",
    "DegreeDaysResult",

    # Utilities
    "validate_coordinates",
    "fahrenheit_to_celsius",
    "celsius_to_fahrenheit",
    "mean_temperature",

    # Exceptions
    "NWSAPIError",
    "InvalidCoordinatesError",

    # Optional providers
    "fetch_meteostat_data",
]
