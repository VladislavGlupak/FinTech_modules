import fire
import questionary
import sqlalchemy
import pandas as pd
from pathlib import Path

# Create a temporary sqlite database
database_connection_string = 'sqlite:///cruddy_database.db'

# Create an engine to interact with the database
engine = sqlalchemy.create_engine(database_connection_string)


"""CREATE

The CREATE operation creates a new table in the database using the given DataFrame.
The table is replaced by the new data if it already exists.
"""


def create_table(engine, table_name, table_data_df):
    table_data_df.to_sql(table_name, engine, index=False, if_exists='replace')


"""READ

The READ operation will read the entire table from the database into a new DataFrame.
Then it will print the DataFrame.
"""


def read_table(engine, table_name):
    results_dataframe = pd.read_sql_table(table_name, con=engine)
    print(f"{table_name} Data:")
    print(results_dataframe)


"""UPDATE

In this section, you will complete the UPDATE operation.

1. Create a function named `update_data` that accepts the following parameters: `engine`, `table_name`, `column`, `old_value`, and `new_value`.

2. Inside the `update-data` function, write a SQL `UPDATE` statement in the form of an f-string. This statement should use the function parameters to update data in the table in the database. Be sure to do the following:

    * In the `UPDATE` statement, include the `UPDATE`, `SET`, and `WHERE` SQL keywords.

    * Include the statement that calls the engine to execute the `UPDATE` statement.

"""


def update_data(engine, table_name, column, old_value, new_value):
    update_sql = """
    UPDATE {table_name}
    SET {column} = {new_value}
    WHERE {column} = {old_value}
    """
    engine.execute(update_sql)


"""DELETE

In this section, you will complete the DELETE operation.

3. Create a function named `delete_data` that accepts the following parameters: `engine`, `table_name`, `column`, and `value`.

4. Inside the `delete_data` function, create a SQL `DELETE` statement in the form of an f-string. This statement should use the function parameters to delete data from the table in the database. Be sure to do the following:

    * In the `DELETE` statement, include the `DELETE FROM` and `WHERE` SQL keywords.

    * Include the statement that calls the engine to execute the `DELETE` statement.
"""


def delete_data(engine, table_name, column, value):
    delete_sql = """
    DELETE FROM {table_name}
    WHERE {column} = {value}
    """
    engine.execute(delete_sql)


def run():
    print("Generating test data for the database...")
    # Create a test DataFrame
    stocks_dataframe = pd.DataFrame({'AAPL': [1, 2], 'GOOG': [3, 4]})
    # Create the database table called 'stocks'
    create_table(engine, 'stocks', stocks_dataframe)

    cruddy_cli_running = True

    while cruddy_cli_running:
        choice = questionary.select(
            "What do you want to do?",
            choices=["Read", "Update", "Delete", "Quit"]
        ).ask()

        if choice == "Read":
            print(f"Available Tables: {engine.table_names()}")
            table_name = questionary.text("Which table would you like to read?").ask()
            read_table(engine, table_name)
        elif choice == "Update":
            # 1. Prompt the user for a table to update.
            table_name = questionary.text("What table would you like to update?").ask()
            # 2. Prompt the user for column to update.
            column = questionary.text("What column would you like to update?").ask()
            # 3. Prompt the user for the old value to find.
            old_value = questionary.text("What is the old value that you want to update?").ask()
            # 4. Prompt the user for the new value.
            new_value = questionary.text("What is the new value that you want to update?").ask()
            # 5. Call the UPDATE operation
            update_data(engine, table_name, column, old_value, new_value)
        elif choice == "Delete":
            # 1. Prompt the user for a table.
            table_name = questionary.text("What table would you like to delete data from?").ask()
            # 2. Prompt the user for the column.
            column = questionary.text("What column is the data in?").ask()
            # 3. Prompt the user for  value to find.
            value = questionary.text("What is the value to delete?").ask()
            # 4. Call the delete operation
            delete_data(engine, table_name, column, value)
        elif choice == "Quit":
            cruddy_cli_running = False
            print("Thank you for using the CRUDdy CLI! Goodbye!")


if __name__ == "__main__":
    fire.Fire(run)
