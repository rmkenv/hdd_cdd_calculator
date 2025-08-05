"""A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD) using NWS API data."""

from .calculator import (
    calculate_degree_days,
    get_degree_days_for_location,
    get_degree_days_for_period,
    DegreeDaysResult,
)
from .exceptions import NWSAPIError, InvalidCoordinatesError

__version__ = "0.1.0"

__all__ = [
    "calculate_degree_days",
    "get_degree_days_for_location",
    "get_degree_days_for_period",
    "DegreeDaysResult",
    "NWSAPIError",
    "InvalidCoordinatesError",
]
