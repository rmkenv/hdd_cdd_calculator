# hdd_cdd_calculator/regression.py
from sklearn.linear_model import LinearRegression
import pandas as pd
from typing import Union

def perform_regression(
    degree_days: Union[pd.Series, list],
    energy_data: Union[pd.Series, list]
) -> LinearRegression:
    """
    Perform linear regression between degree days and energy consumption.

    Parameters:
        degree_days: Series or list of HDD or CDD values
        energy_data: Series or list of energy consumption values

    Returns:
        Trained LinearRegression model
    """
    model = LinearRegression()
    X = pd.Series(degree_days).values.reshape(-1, 1)
    y = pd.Series(energy_data).values
    model.fit(X, y)
    return model
