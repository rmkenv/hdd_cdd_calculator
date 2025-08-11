import pandas as pd
from typing import List, Union
from io import StringIO

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
    # Load CSV with date parsing for potential alignment
    df = pd.read_csv(csv_input, parse_dates=["date"])

    if column not in df.columns:
        raise ValueError(
            f"CSV is missing required '{column}' column. "
            f"Available columns: {list(df.columns)}"
        )

    # Drop missing values from the chosen column
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

    This version returns both the parsed dates and the energy values,
    useful for matching with degree days data.

    Args:
        csv_input: Path to CSV file or file-like object.
        column: Which energy column to load.

    Returns:
        DataFrame with `date` and the chosen energy column.
    """
    df = pd.read_csv(csv_input, parse_dates=["date"])
    if column not in df.columns:
        raise ValueError(
            f"CSV is missing required '{column}' column. "
            f"Available columns: {list(df.columns)}"
        )

    return df[["date", column]].dropna()
