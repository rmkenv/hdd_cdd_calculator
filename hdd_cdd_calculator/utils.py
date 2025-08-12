from typing import Tuple
from .exceptions import InvalidCoordinatesError


def validate_coordinates(lat: float, lon: float) -> Tuple[float, float]:
    """
    Validate and standardize coordinates.

    Args:
        lat: Latitude (-90 to 90)
        lon: Longitude (-180 to 180)

    Returns:
        Tuple of (latitude, longitude) rounded to 4 decimal places (~11 m precision).

    Raises:
        InvalidCoordinatesError: If coordinates are invalid.
    """
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise InvalidCoordinatesError(lat, lon)

    return round(lat, 4), round(lon, 4)


def fahrenheit_to_celsius(temp_f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (temp_f - 32) * 5.0 / 9.0


def celsius_to_fahrenheit(temp_c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return temp_c * 9.0 / 5.0 + 32.0


def mean_temperature(high: float, low: float) -> float:
    """Calculate the mean temperature from high and low values."""
    return (high + low) / 2.0


def calculate_degree_days(
    high_temp: float,
    low_temp: float,
    base_temp: float = 65.0,
    unit: str = "F"
) -> Tuple[float, float]:
    """
    Calculate Heating Degree Days (HDD) and Cooling Degree Days (CDD).

    Args:
        high_temp: Daily high temperature.
        low_temp: Daily low temperature.
        base_temp: Base/reference temperature
                   (default: 65°F if unit='F', 18.3°C if unit='C').
        unit: 'F' for Fahrenheit, 'C' for Celsius. If 'C', temps/base_temp
              will be converted to Fahrenheit before calculations.

    Returns:
        Tuple of (HDD, CDD) — both based on Fahrenheit values.
    """
    unit = unit.upper()
    if unit not in ("F", "C"):
        raise ValueError("unit must be either 'F' or 'C'")

    # Convert to Fahrenheit if needed
    if unit == "C":
        high_temp = celsius_to_fahrenheit(high_temp)
        low_temp = celsius_to_fahrenheit(low_temp)
        base_temp = celsius_to_fahrenheit(base_temp)

    # Sanity check: warn if values are suspicious
    if not (-100 <= high_temp <= 150) or not (-100 <= low_temp <= 150):
        raise ValueError(
            f"Temperature values look suspicious after conversion: "
            f"high={high_temp}, low={low_temp}"
        )

    mean_temp = mean_temperature(high_temp, low_temp)
    hdd = max(0, base_temp - mean_temp)
    cdd = max(0, mean_temp - base_temp)
    return hdd, cdd
