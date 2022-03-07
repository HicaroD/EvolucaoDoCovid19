import pandas as pd

COVID_DATASET_PATH = "datasets/total_cases.csv"

class Forecaster:
    def __init__(self, n):
        self.number_of_days = n

    def fetch_total_cases_from_csv(self):
        covid_dataset = pd.read_csv(COVID_DATASET_PATH, usecols=['World'])
        return covid_dataset

    def predict(self):
        total_cases = self.fetch_total_cases_from_csv()
        print(total_cases)

def main():
    n = int(input("Insira o número de dias: "))

    if n < 0:
        exit()

    forecaster = Forecaster(n)
    forecaster.predict()
main()
