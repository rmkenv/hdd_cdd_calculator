class NWSAPIError(Exception):
    """Raised when there is an error communicating with the NWS API."""

    def __init__(self, message: str, status_code: int = None, url: str = None):
        """
        Args:
            message: Human-readable error message.
            status_code: Optional HTTP status code from the API.
            url: Optional URL of the API request that caused the error.
        """
        self.status_code = status_code
        self.url = url
        super().__init__(self._format_message(message))

    def _format_message(self, message: str) -> str:
        details = message
        if self.status_code:
            details += f" (HTTP {self.status_code})"
        if self.url:
            details += f" | URL: {self.url}"
        return details


class InvalidCoordinatesError(Exception):
    """Raised when geographic coordinates are invalid."""

    def __init__(self, lat: float, lon: float, message: str = None):
        """
        Args:
            lat: Latitude value that caused the error.
            lon: Longitude value that caused the error.
            message: Optional custom message.
        """
        self.lat = lat
        self.lon = lon
        default_message = f"Invalid coordinates: ({lat}, {lon})"
        super().__init__(message or default_message)
