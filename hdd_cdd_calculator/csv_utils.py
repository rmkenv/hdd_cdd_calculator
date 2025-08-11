from hdd_cdd_calculator import get_degree_days_for_period, perform_regression, plot_regression

# Read energy data from CSV file path
energy_values = read_energy_data_from_csv("path/to/energy_data.csv")

# Fetch degree days for the same date range and location
degree_days_results = get_degree_days_for_period(
    lat=40.7128,
    lon=-74.0060,
    start_date="2023-06-01",
    end_date="2023-06-30",
)

hdd_values = [r.hdd for r in degree_days_results]

# Make sure lengths align, handle mismatches as needed

# Perform regression and plot
model = perform_regression(hdd_values, energy_values)
plot_regression(hdd_values, energy_values, model)
