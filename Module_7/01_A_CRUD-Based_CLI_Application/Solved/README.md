# A CRUD-Based CLI Application

In this activity, you'll complete your CLI application by adding functions to update and delete data from a database.

## Instructions

1. Under the “UPDATE” docstring, create a function named `update_data` that accepts the following parameters: `table_name`, `column`, `new_value`, and `old_value`.

2. Inside the `update-data` function, write a SQL `UPDATE` statement in the form of an f-string. This statement should use the function parameters to update data in the table in the database. Be sure to do the following:

    * In the `UPDATE` statement, include the `UPDATE`, `SET`, and `WHERE` SQL keywords.

    * Include the statement that calls the engine to execute the `UPDATE` statement.

3. Under the “DELETE” docstring, create a function named `delete_data` that accepts the following parameters: `table_name`, `column`, and `value`.

4. Inside the `delete_data` function, create a SQL `DELETE` statement in the form of an f-string. This statement should use the function parameters to delete data from the table in the database. Be sure to do the following:

    * In the `DELETE` statement, include the `DELETE FROM` and `WHERE` SQL keywords.

    * Include the statement that calls the engine to execute the `DELETE` statement.
