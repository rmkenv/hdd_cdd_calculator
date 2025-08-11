from typing import Tuple
from .exceptions import InvalidCoordinatesError

# -------------------------
# Coordinate Validation
# -------------------------
def validate_coordinates(lat: float, lon: float) -> Tuple[float, float]:
    """
    Validate and standardize coordinates.

    Args:
        lat: Latitude (-90 to 90)
        lon: Longitude (-180 to 180)

    Returns:
        Tuple of (latitude, longitude) rounded to 4 decimal places.

    Raises:
        InvalidCoordinatesError: If coordinates are invalid.
    """
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise InvalidCoordinatesError(f"Invalid coordinates: ({lat}, {lon})")

    # Round to 4 decimal places (~11 meters precision)
    return round(lat, 4), round(lon, 4)

# -------------------------
# Temperature Conversions
# -------------------------
def fahrenheit_to_celsius(temp_f: float) -> float:
    """Convert temperature from °F to °C."""
    return (temp_f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(temp_c: float) -> float:
    """Convert temperature from °C to °F."""
    return (temp_c * 9.0 / 5.0) + 32

# -------------------------
# Temperature Calculations
# -------------------------
def mean_temperature(high: float, low: float) -> float:
    """Return the average of the daily high and low temperatures."""
    return (high + low) / 2

# -------------------------
# Degree Day Calculations
# -------------------------
def calculate_degree_days(high_temp: float, low_temp: float, base_temp: float = 65.0) -> Tuple[float, float]:
    """
    Calculate Heating Degree Days (HDD) and Cooling Degree Days (CDD)
    based on high and low temperatures.

    Args:
        high_temp: Daily high temperature (same unit as base_temp)
        low_temp: Daily low temperature (same unit as base_temp)
        base_temp: Base/reference temperature (default: 65°F)

    Returns:
        Tuple of (HDD, CDD)
    """
    mean_temp = mean_temperature(high_temp, low_temp)
    hdd = max(0, base_temp - mean_temp)
    cdd = max(0, mean_temp - base_temp)
    return hdd, cdd
