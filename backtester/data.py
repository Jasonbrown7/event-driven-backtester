import pandas as pd

class CsvDataHandler:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path, parse_dates=True, index_col='Date')
        self.data.columns = [col.lower().replace(' ', '_').replace('/', '_') for col in self.data.columns]
