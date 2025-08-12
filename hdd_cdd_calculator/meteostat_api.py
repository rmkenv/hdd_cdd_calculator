from meteostat import Point, Daily
from datetime import datetime
from typing import List, NamedTuple
from .utils import calculate_degree_days, validate_coordinates, celsius_to_fahrenheit
from .exceptions import NWSAPIError

class DegreeDaysResult(NamedTuple):
    date: str
    high_temp: float
    low_temp: float
    mean_temp: float
    hdd: float
    cdd: float

def fetch_meteostat_data(
    lat: float,
    lon: float,
    start_date: str,
    end_date: str,
    base_temp: float = 65.0
) -> List[DegreeDaysResult]:
    """
    Fetch Meteostat daily temps, convert to °F, then calculate HDD/CDD with °F base temp.
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
            t_min_c = row["tmin"]
            t_max_c = row["tmax"]
            if t_min_c is None or t_max_c is None:
                continue  # skip incomplete days

            # ✅ Convert C → F
            t_min_f = celsius_to_fahrenheit(t_min_c)
            t_max_f = celsius_to_fahrenheit(t_max_c)
            mean_temp_f = (t_max_f + t_min_f) / 2

            # HDD/CDD calc now consistent with °F base_temp
            hdd, cdd = calculate_degree_days(t_max_f, t_min_f, base_temp)

            results.append(
                DegreeDaysResult(
                    date.strftime("%Y-%m-%d"),
                    t_max_f,
                    t_min_f,
                    mean_temp_f,
                    hdd,
                    cdd,
                )
            )

        return results

    except Exception as e:
        raise NWSAPIError(f"Failed to fetch Meteostat data: {str(e)}")
