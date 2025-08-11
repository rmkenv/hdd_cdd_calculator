from meteostat import Point, Daily
from datetime import datetime
from typing import List, NamedTuple
from .utils import calculate_degree_days, validate_coordinates
from .exceptions import NWSAPIError

class DegreeDaysResult(NamedTuple):
    date: str
    high_temp: float
    low_temp: float
    mean_temp: float
    hdd: float
    cdd: float

def fetch_meteostat_data(lat: float, lon: float, start_date: str, end_date: str, base_temp: float = 65.0) -> List[DegreeDaysResult]:
    """
    Fetch historical temperature data from Meteostat and calculate HDD/CDD.
    
    Args:
        lat: Latitude (-90 to 90)
        lon: Longitude (-180 to 180)
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        base_temp: Base temperature for calculations (default: 65°F)
    
    Returns:
        List of DegreeDaysResult
    
    Raises:
        NWSAPIError: if data fetching fails or other errors occur.
    """
    lat, lon = validate_coordinates(lat, lon)

    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        location = Point(lat, lon)
        data = Daily(location, start, end)
        df = data.fetch()

        results = []
        for date, row in df.iterrows():
            t_min = row['tmin']
            t_max = row['tmax']
            if t_min is None or t_max is None:
                continue  # Skip incomplete data
            hdd, cdd = calculate_degree_days(t_max, t_min, base_temp)
            mean_temp = (t_max + t_min) / 2
            results.append(
                DegreeDaysResult(date.strftime("%Y-%m-%d"), t_max, t_min, mean_temp, hdd, cdd)
            )
        return results

    except Exception as e:
        raise NWSAPIError(f"Failed to fetch Meteostat data: {str(e)}")
