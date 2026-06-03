import streamlit as st

from repositories.csv_repository import CsvRepository
from repositories.sqlite_repository import SQLiteRepository


class DataExplorerTab:
    """Streamlit tab that displays the selected repository."""

    def __init__(self, repository, source_label):
        self.repository = repository
        self.source_label = source_label

    def display(self):
        st.subheader("Data Explorer")
        st.write(f"Selected source: **{self.source_label}**")

        if isinstance(self.repository, SQLiteRepository):
            self._display_sqlite_source()
        elif isinstance(self.repository, CsvRepository):
            self._display_csv_source()
        else:
            st.warning("This source type is not supported yet.")

    def _display_sqlite_source(self):
        tables = self.repository.list_sources()

        if not tables:
            st.info("This SQLite database does not have any tables.")
            return

        selected_table = st.selectbox("Choose a table", tables)
        preview = self.repository.preview_data(selected_table)
        columns = self.repository.get_columns(selected_table)
        row_count = self.repository.get_row_count(selected_table)
        query = self.repository.build_preview_query(selected_table)

        st.markdown("**SQL query being executed:**")
        st.code(query, language="sql")

        self._show_basic_details(columns, row_count)
        st.dataframe(preview, use_container_width=True)

    def _display_csv_source(self):
        st.info("CSV files are flat files. They contain rows and columns, but they do not contain separate tables.")

        preview = self.repository.preview_data()
        columns = self.repository.get_columns()
        row_count = self.repository.get_row_count()

        self._show_basic_details(columns, row_count)
        st.dataframe(preview, use_container_width=True)

    def _show_basic_details(self, columns, row_count):
        st.markdown(f"**Row count:** {row_count}")
        st.markdown("**Column names:**")
        st.write(", ".join(columns))
