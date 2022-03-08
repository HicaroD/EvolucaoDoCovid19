import unittest
import forecaster
import pandas as pd

class TestLinearRegressionModel(unittest.TestCase):
    def test_const_value(self):
        forecaster_ = forecaster.Forecaster("datasets/dummy_dataset.csv")
        number_of_cases = forecaster_.fetch_number_of_cases_column()

        linear_regression_model = forecaster.LinearRegressionModel()
        self.const, _ = linear_regression_model.get_formula_data(number_of_cases)

        self.assertEqual(round(self.const, 1), 2.2)

if __name__ == "__main__":
    unittest.main()
