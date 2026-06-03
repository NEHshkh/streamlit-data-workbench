# Streamlit Data Workbench: Data Explorer

This project is my Milestone 1 Streamlit Data Workbench. The app lets a user explore structured data from three sources:

- Chinook SQLite database
- A small teaching SQLite database
- A public CSV-style dataset saved as `sample_data.csv`

The main goal is to preview data, see column names, count rows, and understand how different data sources are organized.

## Project Structure

```text
streamlit_data_workbench/
├── app.py
├── repositories/
│   ├── data_repository.py
│   ├── sqlite_repository.py
│   └── csv_repository.py
├── data/
│   ├── Chinook_Sqlite.sqlite
│   ├── teaching_database.sqlite
│   └── sample_data.csv
├── tabs/
│   └── data_explorer_tab.py
├── requirements.txt
└── README.md
```

## How to Run the App

1. Open a terminal in the `streamlit_data_workbench` folder.
2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Start the Streamlit app:

```bash
streamlit run app.py
```

4. Use the dropdown to choose one of the data sources.

## What the App Does

For SQLite databases, the app:

- Lists available tables
- Lets the user select one table
- Shows a preview of the selected table
- Shows the column names
- Shows the row count
- Shows the SQL query being used

For the CSV file, the app:

- Shows a preview of the file
- Shows the column names
- Shows the row count
- Explains that CSV files do not contain tables

## Repository Pattern

This project uses a repository pattern. The Streamlit page does not directly open SQLite or CSV files. Instead, it asks repository objects for the data.

The classes are:

- `DataRepository`: the parent class that defines the methods every repository should have
- `SQLiteRepository`: handles SQLite tables and SQL queries
- `CsvRepository`: handles the CSV file

This keeps the app more organized because the user interface and the data access code are separated.

## Reflection Questions

### 1. What is the difference between a CSV file and a relational database?

A CSV file is a flat text file with rows and columns. It usually stores one dataset at a time. A relational database can store many related tables, and those tables can connect to each other with keys. A database can also run SQL queries, count rows, filter data, and manage larger sets of information more safely.

### 2. Why is a repository pattern useful?

The repository pattern is useful because it separates the app screen from the data access code. The Streamlit app does not need to know how SQLite or CSV files work. It just calls methods like `preview_data()` or `get_columns()`. This makes the code easier to read, test, and change later.

### 3. How does this project connect to big data?

Big data work starts with understanding the data. Before a person can analyze data or build a model, they need to know what tables exist, what columns are available, and how many rows are in the data. This project is a small version of that same process.

### 4. Why is exploring data important before analysis begins?

Exploring data helps find what information is available and whether the data has problems. It can show missing columns, unexpected values, confusing names, or tables that are not useful for the question being asked. Good exploration helps prevent mistakes during analysis.

### 5. What object-oriented techniques did you apply?

I used classes, inheritance, and method overriding. `DataRepository` is the base class. `SQLiteRepository` and `CsvRepository` inherit from it and provide their own versions of the required methods. I also used objects in the Streamlit app so each data source has its own repository.

## Notes

The code is intentionally simple for a first milestone. I focused on readable classes, clear method names, and comments that explain the OOP and repository pattern parts.
