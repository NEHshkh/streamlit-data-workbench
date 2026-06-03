from pathlib import Path

import streamlit as st

from repositories.csv_repository import CsvRepository
from repositories.sqlite_repository import SQLiteRepository
from tabs.data_explorer_tab import DataExplorerTab


def build_repositories():
    """Create the available repositories for the app."""
    data_folder = Path(__file__).parent / "data"

    return {
        "Chinook SQLite Database": SQLiteRepository(data_folder / "Chinook_Sqlite.sqlite"),
        "Teaching SQLite Database": SQLiteRepository(data_folder / "teaching_database.sqlite"),
        "Public CSV Dataset": CsvRepository(data_folder / "sample_data.csv"),
    }


def main():
    st.set_page_config(page_title="Streamlit Data Workbench", layout="wide")

    st.title("Streamlit Data Workbench")
    st.write("Milestone 1: Data Explorer")

    repositories = build_repositories()
    selected_source = st.selectbox("Select a data source", list(repositories.keys()))

    data_explorer, = st.tabs(["Data Explorer"])

    with data_explorer:
        tab = DataExplorerTab(repositories[selected_source], selected_source)
        tab.display()


if __name__ == "__main__":
    main()
