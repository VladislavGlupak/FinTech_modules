import fire
import questionary
import sqlalchemy
import pandas as pd
from pathlib import Path

# Create a temporary sqlite database
database_connection_string = 'sqlite:///'

# Create an engine to interact with the database
engine = sqlalchemy.create_engine(database_connection_string)

# Create a test DataFrame
stocks_dataframe = pd.DataFrame({'AAPL': [1, 2], 'GOOG': [3, 4]})

def create_table(engine, table_name, table_data_df):
    table_data_df.to_sql(table_name, engine, index=False, if_exists='replace')
    
def confirm_tables(engine):
    tables = engine.table_names()
    print(f"The tables in the database are: {tables}")
    
def run():
    """The main function for running the application."""

    # Prompt the user for the table name
    table_name = questionary.text("What name would you like to use for your table?").ask()

    # Create the table in the database
    create_table(engine, table_name, stocks_dataframe)

    # Confirm the table in the database
    confirm_tables(engine)

if __name__ == "__main__":
    fire.Fire(run)