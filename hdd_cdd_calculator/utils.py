from typing import Tuple
from .exceptions import InvalidCoordinatesError

def validate_coordinates(lat: float, lon: float) -> Tuple[float, float]:
    """
    Validate and standardize coordinates.
    
    Args:
        lat: Latitude
        lon: Longitude
    
    Returns:
        Tuple of (latitude, longitude)
    
    Raises:
        InvalidCoordinatesError: If coordinates are invalid
    """
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise InvalidCoordinatesError(f"Invalid coordinates: ({lat}, {lon})")
    
    # Round to 4 decimal places (~11 meter precision)
    return round(lat, 4), round(lon, 4)
