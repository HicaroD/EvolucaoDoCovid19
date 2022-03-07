import pandas as pd

COVID_DATASET_PATH = "datasets/total_cases.csv"

class Forecaster:
    def __init__(self, n):
        self.number_of_days = n
        self.covid_dataset = pd.read_csv(COVID_DATASET_PATH, usecols=['date', 'World'])

    def fetch_number_of_cases_column(self):
        return self.covid_dataset.iloc[:, 1]

    def fetch_date_column(self):
        return self.covid_dataset.iloc[:, :-1]

    def predict(self):
        date, number_of_cases = self.fetch_date_column(), self.fetch_number_of_cases_column()
        print(date, number_of_cases)

def main():
    n = int(input("Insira o número de dias: "))

    if n < 0:
        exit()

    forecaster = Forecaster(n)
    forecaster.predict()
main()
