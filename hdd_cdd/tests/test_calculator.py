import unittest
from hdd_cdd import calculate_degree_days, validate_coordinates
from hdd_cdd.exceptions import InvalidCoordinatesError
from hdd_cdd.calculator import get_forecast_url


class TestCalculator(unittest.TestCase):

    def test_calculate_degree_days(self):
        # Test basic calculations (base temp 65°F)
        self.assertEqual(calculate_degree_days(70, 50), (10, 0))  # Mean 60
        self.assertEqual(calculate_degree_days(80, 60), (0, 5))   # Mean 70
        self.assertEqual(calculate_degree_days(65, 65), (0, 0))   # Mean 65

        # Test with different base temperature
        self.assertEqual(calculate_degree_days(70, 50, base_temp=60), (5, 0))  # Mean 60

    def test_validate_coordinates_valid(self):
        # Should round and return valid coordinates
        lat, lon = validate_coordinates(40.712776, -74.005974)
        self.assertEqual(lat, 40.7128)
        self.assertEqual(lon, -74.0060)

    def test_validate_coordinates_invalid(self):
        with self.assertRaises(InvalidCoordinatesError):
            validate_coordinates(-100, 0)   # Invalid latitude
        with self.assertRaises(InvalidCoordinatesError):
            validate_coordinates(0, 200)    # Invalid longitude

    def test_get_forecast_url_invalid_coords(self):
        # get_forecast_url() should also raise for invalid values
        with self.assertRaises(InvalidCoordinatesError):
            get_forecast_url(-100, 0)
        with self.assertRaises(InvalidCoordinatesError):
            get_forecast_url(0, 200)


if __name__ == '__main__':
    unittest.main()
