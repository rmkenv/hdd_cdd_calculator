import requests
from datetime import datetime
from typing import List, NamedTuple, Tuple
from .exceptions import NWSAPIError, InvalidCoordinatesError
from .utils import validate_coordinates, calculate_degree_days

USER_AGENT = "HDD-CDD-Calculator/0.1 (https://github.com/rmkenv/hdd_cdd_calculator)"

class DegreeDaysResult(NamedTuple):
    """Container for degree days calculation results."""
    date: str
    high_temp: float
    low_temp: float
    mean_temp: float
    hdd: float
    cdd: float

def get_forecast_url(lat: float, lon: float) -> str:
    """
    Get the forecast URL for given coordinates from the NWS API.
    
    Args:
        lat: Latitude
        lon: Longitude
    
    Returns:
        Forecast URL for the location
    
    Raises:
        InvalidCoordinatesError: If coordinates are invalid
        NWSAPIError: If there's an error with the NWS API
    """
    lat, lon = validate_coordinates(lat, lon)

    try:
        url = f"https://api.weather.gov/points/{lat:.4f},{lon:.4f}"
        response = requests.get(url, headers={"User-Agent": USER_AGENT})
        response.raise_for_status()
        data = response.json()
        return data['properties']['forecast']
    except requests.exceptions.RequestException as e:
        raise NWSAPIError(f"Failed to get forecast URL: {str(e)}")

def get_daily_temps(forecast_url: str) -> List[Tuple[str, float, float]]:
    """
    Get daily high and low temperatures from NWS forecast data.
    
    Args:
        forecast_url: URL to NWS forecast data
    
    Returns:
        List of tuples containing (date, high_temp, low_temp)
    
    Raises:
        NWSAPIError: If there's an error with the NWS API
    """
    try:
        response = requests.get(forecast_url, headers={"User-Agent": USER_AGENT})
        response.raise_for_status()
        data = response.json()
        
        daily_temps = {}
        for period in data['properties']['periods']:
            start_time = period['startTime']
            date = start_time.split('T')[0]
            temp = period['temperature']
            is_daytime = period['isDaytime']
            
            if date not in daily_temps:
                daily_temps[date] = {'high': None, 'low': None}
            
            if is_daytime:
                if daily_temps[date]['high'] is None or temp > daily_temps[date]['high']:
                    daily_temps[date]['high'] = temp
            else:
                if daily_temps[date]['low'] is None or temp < daily_temps[date]['low']:
                    daily_temps[date]['low'] = temp
        
        # Filter and prepare list results
        result = []
        for date, temps in sorted(daily_temps.items()):
            if temps['high'] is not None and temps['low'] is not None:
                result.append((date, temps['high'], temps['low']))
        
        return result
    except requests.exceptions.RequestException as e:
        raise NWSAPIError(f"Failed to get forecast data: {str(e)}")

def get_degree_days_for_location(lat: float, lon: float, base_temp: float = 65.0) -> List[DegreeDaysResult]:
    """
    Get degree days for a specific location.
    
    Args:
        lat: Latitude
        lon: Longitude
        base_temp: Base temperature (default 65°F)
    
    Returns:
        List of DegreeDaysResult objects
    
    Raises:
        InvalidCoordinatesError: If coordinates are invalid
        NWSAPIError: If there's an API error
    """
    forecast_url = get_forecast_url(lat, lon)
    daily_temps = get_daily_temps(forecast_url)
    
    results = []
    for date, high, low in daily_temps:
        hdd, cdd = calculate_degree_days(high, low, base_temp)
        mean_temp = (high + low) / 2
        results.append(DegreeDaysResult(date, high, low, mean_temp, hdd, cdd))
    
    return results

def get_degree_days_for_period(lat: float, lon: float, start_date: str, end_date: str, base_temp: float = 65.0) -> List[DegreeDaysResult]:
    """
    Get degree days for a location and date range.
    
    Args:
        lat: Latitude
        lon: Longitude
        start_date: Start date in YYYY-MM-DD
        end_date: End date in YYYY-MM-DD
        base_temp: Base temperature for HDD/CDD calculations
    
    Returns:
        List of DegreeDaysResult objects for the specified period
    
    Raises:
        InvalidCoordinatesError: If coordinates are invalid
        NWSAPIError: If there's an API error
    """
    all_results = get_degree_days_for_location(lat, lon, base_temp)
    filtered = [
        result for result in all_results
        if start_date <= result.date <= end_date
    ]
    return filtered
