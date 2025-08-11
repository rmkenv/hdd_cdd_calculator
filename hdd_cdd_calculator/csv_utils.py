# hdd_cdd_calculator/csv_utils.py
import pandas as pd
from typing import List, Tuple, Union
from io import StringIO
from hdd_cdd_calculator import DegreeDaysResult  # For typing


def read_energy_data_from_csv(
    csv_input: Union[str, StringIO],
    column: str = "kwh"
) -> List[float]:
    """
    Read energy consumption data from a CSV file or file-like object.

    Expected CSV format:
        date, kwh, mmbtu, gal

    Args:
        csv_input: Path to CSV file or file-like object (StringIO).
        column: Which energy column to load ("kwh", "mmbtu", or "gal"), defaults to "kwh".

    Returns:
        List of numeric energy consumption values from the selected column.

    Raises:
        ValueError: If the requested column is missing or contains no data.
    """
    df = pd.read_csv(csv_input, parse_dates=["date"])
    if column not in df.columns:
        raise ValueError(
            f"CSV is missing required '{column}' column. "
            f"Available columns: {list(df.columns)}"
        )

    energy_series = df[column].dropna()
    if energy_series.empty:
        raise ValueError(f"The '{column}' column contains no data.")

    return energy_series.tolist()


def read_energy_data_with_dates(
    csv_input: Union[str, StringIO],
    column: str = "kwh"
) -> pd.DataFrame:
    """
    Read dates and energy consumption data from CSV.

    Returns a DataFrame with `date` and the selected column.

    Args:
        csv_input: Path or file-like object for CSV.
        column: Which energy column to load.

    Returns:
        DataFrame with `date` and energy column.
    """
    df = pd.read_csv(csv_input, parse_dates=["date"])
    if column not in df.columns:
        raise ValueError(
            f"CSV is missing required '{column}' column. "
            f"Available columns: {list(df.columns)}"
        )
    return df[["date", column]].dropna()


def align_energy_with_degree_days(
    degree_days: List[DegreeDaysResult],
    csv_input: Union[str, StringIO],
    energy_column: str = "kwh",
    degree_day_type: str = "hdd"
) -> Tuple[List[float], List[float]]:
    """
    Align energy CSV data with degree days by matching on date.

    Args:
        degree_days: List of DegreeDaysResult namedtuples (with `date` field).
        csv_input: Path or file-like object to CSV containing energy data.
        energy_column: Name of the energy data column to use ("kwh", "mmbtu", "gal").
        degree_day_type: "hdd" or "cdd" — which degree day value to align.

    Returns:
        (energy_values, degree_day_values): Both lists matched by date.

    Raises:
        ValueError: If no data overlaps or columns are missing.
    """
    # Convert degree days to DataFrame
    dd_df = pd.DataFrame([dd._asdict() for dd in degree_days])
    dd_df["date"] = pd.to_datetime(dd_df["date"])

    # Read CSV with parsed dates
    energy_df = pd.read_csv(csv_input, parse_dates=["date"])
    if energy_column not in energy_df.columns:
        raise ValueError(
            f"CSV missing '{energy_column}' column. Found columns: {list(energy_df.columns)}"
        )

    # Merge on date
    merged = pd.merge(dd_df, energy_df[["date", energy_column]], on="date", how="inner")
    if merged.empty:
        raise ValueError("No overlapping dates between degree days and energy data.")

    merged = merged.sort_values("date")
    degree_day_values = merged[degree_day_type].tolist()
    energy_values = merged[energy_column].tolist()

    return energy_values, degree_day_values
