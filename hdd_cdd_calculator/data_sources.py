from .calculator import get_degree_days_for_period as get_nws_data
from .meteostat_api import fetch_meteostat_data

def get_degree_days(lat, lon, start_date, end_date, source="nws", base_temp=65.0):
    """
    Retrieve HDD/CDD data from the specified source.

    Args:
        lat: Latitude
        lon: Longitude
        start_date: YYYY-MM-DD
        end_date: YYYY-MM-DD
        source: "nws" or "meteostat"
        base_temp: Base temperature for degree day calculation (°F)

    Returns:
        List of DegreeDaysResult
    """
    if source == "nws":
        return get_nws_data(lat, lon, start_date, end_date, base_temp)
    elif source == "meteostat":
        return fetch_meteostat_data(lat, lon, start_date, end_date, base_temp)
    else:
        raise ValueError("Unknown source. Choose 'nws' or 'meteostat'")
