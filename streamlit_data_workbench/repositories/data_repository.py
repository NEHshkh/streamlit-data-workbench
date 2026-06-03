from abc import ABC, abstractmethod


class DataRepository(ABC):
    """Base class for all data repositories.

    The repository pattern keeps the Streamlit pages from knowing how files are
    opened. The page asks for data, and the repository handles the details.
    """

    @abstractmethod
    def list_sources(self):
        """Return tables or source names that can be explored."""
        pass

    @abstractmethod
    def preview_data(self, source_name=None, limit=100):
        """Return a small preview of the data."""
        pass

    @abstractmethod
    def get_columns(self, source_name=None):
        """Return column names for the selected data."""
        pass

    @abstractmethod
    def get_row_count(self, source_name=None):
        """Return the number of rows in the selected data."""
        pass
