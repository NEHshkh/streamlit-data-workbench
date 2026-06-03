import pandas as pd

from repositories.data_repository import DataRepository


class CsvRepository(DataRepository):
    """Repository for reading data from one CSV file."""

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self._data = None

    def _load_data(self):
        if self._data is None:
            self._data = pd.read_csv(self.csv_path)

        return self._data

    def list_sources(self):
        # A CSV is one flat file, so it does not have tables like SQLite.
        return ["CSV file"]

    def preview_data(self, source_name=None, limit=100):
        data = self._load_data()
        return data.head(limit)

    def get_columns(self, source_name=None):
        data = self._load_data()
        return list(data.columns)

    def get_row_count(self, source_name=None):
        data = self._load_data()
        return len(data)
