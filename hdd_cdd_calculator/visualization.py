import matplotlib.pyplot as plt
import pandas as pd
from typing import Optional, Union

def plot_regression(
    degree_days: Union[pd.Series, list],
    energy_data: Union[pd.Series, list],
    model,
    save_path: Optional[str] = None,
    show: bool = True
):
    """
    Plot degree days vs. energy consumption along with the regression line.

    Args:
        degree_days: Sequence of degree day values (list or Pandas Series)
        energy_data: Sequence of energy consumption values (list or Pandas Series)
        model: Trained regression model (e.g., scikit-learn LinearRegression)
        save_path: Optional file path to save the plot (e.g., 'examples/regression_plot.png')
        show: Whether to display the plot window (default True)
    """
    # Convert to Pandas Series for consistency
    dd_series = pd.Series(degree_days)
    en_series = pd.Series(energy_data)

    # Scatter plot data points
    plt.figure(figsize=(8, 5))
    plt.scatter(dd_series, en_series, label='Data Points', color='blue')

    # Regression line
    plt.plot(
        dd_series,
        model.predict(dd_series.values.reshape(-1, 1)),
        color='red',
        label='Regression Line'
    )

    plt.xlabel('Degree Days')
    plt.ylabel('Energy Consumption')
    plt.title('Degree Days vs Energy Consumption')
    plt.legend()

    # Save if requested
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"[INFO] Plot saved to {save_path}")

    # Show the plot if desired
    if show:
        plt.show()
    else:
        plt.close()
