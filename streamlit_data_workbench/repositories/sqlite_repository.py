import sqlite3

import pandas as pd

from repositories.data_repository import DataRepository


class SQLiteRepository(DataRepository):
    """Repository for reading data from a SQLite database."""

    def __init__(self, database_path):
        self.database_path = database_path

    def _connect(self):
        return sqlite3.connect(self.database_path)

    def list_sources(self):
        query = """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            ORDER BY name;
        """

        with self._connect() as connection:
            table_rows = connection.execute(query).fetchall()

        return [row[0] for row in table_rows]

    def preview_data(self, source_name=None, limit=100):
        query = self.build_preview_query(source_name, limit)

        with self._connect() as connection:
            return pd.read_sql_query(query, connection)

    def get_columns(self, source_name=None):
        query = f"PRAGMA table_info({self._safe_table_name(source_name)});"

        with self._connect() as connection:
            column_rows = connection.execute(query).fetchall()

        return [row[1] for row in column_rows]

    def get_row_count(self, source_name=None):
        query = f"SELECT COUNT(*) FROM {self._safe_table_name(source_name)};"

        with self._connect() as connection:
            count = connection.execute(query).fetchone()[0]

        return count

    def build_preview_query(self, source_name, limit=100):
        table_name = self._safe_table_name(source_name)
        return f"SELECT *\nFROM {table_name}\nLIMIT {limit};"

    def _safe_table_name(self, source_name):
        """Only allow table names that actually exist in this database."""
        if source_name not in self.list_sources():
            raise ValueError("Please select a valid table.")

        return f'"{source_name}"'
