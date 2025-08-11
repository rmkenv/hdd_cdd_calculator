import matplotlib.pyplot as plt

def plot_regression(degree_days, energy_data, model):
    """
    Plot degree days vs. energy consumption along with the regression line.
    
    Args:
        degree_days: A sequence (e.g., list or Pandas Series) of degree day values.
        energy_data: A sequence of corresponding energy consumption values.
        model: A trained regression model (e.g., from scikit-learn).
    """
    plt.scatter(degree_days, energy_data, label='Data Points')
    plt.plot(degree_days, model.predict(degree_days.values.reshape(-1, 1)), color='red', label='Regression Line')
    plt.xlabel('Degree Days')
    plt.ylabel('Energy Consumption')
    plt.legend()
    plt.show()
