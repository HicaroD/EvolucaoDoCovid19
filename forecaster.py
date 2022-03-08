import pandas as pd
import numpy as np
import statsmodels.api as sm
import math

COVID_DATASET_PATH = "datasets/total_cases.csv"

class LinearRegressionModel:
    def unlog(self, value):
        return math.exp(value)

    def apply_ordinary_least_squares(self, log_of_number_of_cases, days):
        model = sm.OLS(log_of_number_of_cases, days)
        result = model.fit()
        return result

    def get_formula_data(self, number_of_cases_column):
        log_of_number_of_cases = np.log(number_of_cases_column).to_list()

        days = np.arange(len(log_of_number_of_cases)).tolist()
        days = sm.add_constant(days)

        result = self.apply_ordinary_least_squares(log_of_number_of_cases, days)

        const, x1 = self.unlog(result.params[0]), self.unlog(result.params[1])
        return const, x1

class Forecaster:
    def __init__(self, dataset_path):
        self.covid_dataset = pd.read_csv(dataset_path)

    def fetch_number_of_cases_column(self):
        return self.covid_dataset['World']

    def predict(self, days_from_user):
        linear_regression_model = LinearRegressionModel()
        number_of_cases = self.fetch_number_of_cases_column()
        const, x1 = linear_regression_model.get_formula_data(number_of_cases)

        for day in range(1, days_from_user + 1):
            value = int(const * math.pow(x1, day))
            print(day, '->', value)


def main():
    n = int(input("Insira o número de dias: "))

    if n < 0:
        exit()

    forecaster = Forecaster(COVID_DATASET_PATH)
    forecaster.predict(n)

if __name__ == "__main__":
    main()
