from .calculator import get_degree_days_for_period as get_nws_data
from .meteostat_api import fetch_meteostat_data
from .utils import celsius_to_fahrenheit  # make sure this exists in your utils

def get_degree_days(lat, lon, start_date, end_date, source="nws", base_temp=65.0):
    """
    Retrieve HDD/CDD data from the specified source and ensure temps are in Fahrenheit.

    Args:
        lat: Latitude
        lon: Longitude
        start_date: YYYY-MM-DD
        end_date: YYYY-MM-DD
        source: "nws" or "meteostat"
        base_temp: Base temperature for degree day calculation (°F)

    Returns:
        List of DegreeDaysResult with temperatures in °F
    """
    if source == "nws":
        results = get_nws_data(lat, lon, start_date, end_date, base_temp)
    elif source == "meteostat":
        results = fetch_meteostat_data(lat, lon, start_date, end_date, base_temp)
        # Convert C → F for consistency
        for r in results:
            r.high_temp = celsius_to_fahrenheit(r.high_temp)
            r.low_temp = celsius_to_fahrenheit(r.low_temp)
    else:
        raise ValueError("Unknown source. Choose 'nws' or 'meteostat'")

    return results
