import unittest
from hdd_cdd.calculator import calculate_degree_days
from hdd_cdd.exceptions import InvalidCoordinatesError

class TestCalculator(unittest.TestCase):
    def test_calculate_degree_days(self):
        # Test basic calculations
        self.assertEqual(calculate_degree_days(70, 50), (10, 0))  # Mean 60
        self.assertEqual(calculate_degree_days(80, 60), (0, 5))    # Mean 70
        self.assertEqual(calculate_degree_days(65, 65), (0, 0))    # Mean 65
        
        # Test with different base temperature
        self.assertEqual(calculate_degree_days(70, 50, 60), (5, 0))  # Mean 60
        
    def test_invalid_coordinates(self):
        from hdd_cdd.calculator import get_forecast_url
        with self.assertRaises(InvalidCoordinatesError):
            get_forecast_url(-100, 0)  # Invalid latitude
        with self.assertRaises(InvalidCoordinatesError):
            get_forecast_url(0, 200)   # Invalid longitude

if __name__ == '__main__':
    unittest.main()
