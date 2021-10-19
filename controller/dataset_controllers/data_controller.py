import pandas as pd
import os


class DataController:

    def __init__(self):
        abs_path = os.path.abspath("data/housing.csv")
        self.df = pd.read_csv(abs_path)

    def get_dataset(self):
        return self.df
