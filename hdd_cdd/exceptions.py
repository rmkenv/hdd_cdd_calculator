class NWSAPIError(Exception):
    """Exception raised for errors when interacting with the NWS API."""
    pass

class InvalidCoordinatesError(Exception):
    """Exception raised for invalid geographic coordinates."""
    pass
