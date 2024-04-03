import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """Create and return a database connection."""
    try:
        return sqlite3.connect(db_file)
    except Error as e:
        print(f"Error connecting to database: {e}")


def create_table(conn):
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS assurance_survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sector TEXT,
            location TEXT,
            role TEXT,
            responsibilities TEXT,
            assurance_meaning TEXT,
            governance_requirements TEXT,
            assurance_methods TEXT,
            properties_assured TEXT,
            assurance_execution TEXT,
            existing_resources TEXT,
            ethics_framework TEXT,
            ethics_definition TEXT,
            framework_development TEXT,
            biggest_challenges TEXT,
            type_of_support TEXT,
            sorted_support_types TEXT,
            ethical_issues TEXT,
            value_ethical_principles INTEGER,
            importance_gemini_principles INTEGER,
            difficulty_operationalizing INTEGER,
            satisfaction_integration INTEGER,
            additional_insights TEXT,
            workshop_interest BOOLEAN,
            agree_integration INTEGER,
            agree_communicate INTEGER,
            agree_linking INTEGER,
            lifecycle_stages TEXT,
            satisfaction_docs INTEGER,
            email TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """

    try:
        conn.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(f"Error creating table: {e}")


def insert_survey_result(conn, table_name, data):
    # 'data' is a dictionary where keys are column names and values are the corresponding data

    # Prepare the SQL statement dynamically based on the provided data
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Execute the insert operation
    cur = conn.cursor()
    cur.execute(sql, tuple(data.values()))
    conn.commit()


# Function to query data from the database
def query_data(conn, column_name):
    df = pd.read_sql(f"SELECT {column_name} FROM assurance_survey", conn)
    return df
