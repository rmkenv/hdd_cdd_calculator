"""
A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD).

Currently supports fetching forecast temperature data from the U.S. National Weather Service (NWS) API
to calculate HDD and CDD values. Designed with modularity, allowing additional
weather data providers (e.g., Meteostat) to be integrated easily.

Public API:
    - Degree Days calculation from daily high/low temps
    - Retrieve HDD/CDD for a single location or a date range
    - Utility functions for coordinate validation and temperature conversions
"""

from .calculator import (
    get_degree_days_for_location,
    get_degree_days_for_period,
    DegreeDaysResult,
)
from .utils import (
    validate_coordinates,
    calculate_degree_days,
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
    mean_temperature,
)
from .exceptions import (
    NWSAPIError,
    InvalidCoordinatesError,
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
]
