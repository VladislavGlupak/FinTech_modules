"""Pathways to Success Part 2."""
# @TODO: Import the csv library
# YOUR CODE HERE!
import csv
from pathlib import Path

# @TODO: Create a path to the csv file called `quarterly_data.csv`
# YOUR CODE HERE!
file_path = Path('quarterly_data.csv')

# @TODO: Open the csv path, read the data, and print each row
# YOUR CODE HERE!

with open(file_path) as csv_file:
    data = csv.reader(csv_file)
    counter = 0
    for line in data:
        print(line)
        counter = counter + 1
    print(counter)

"""Extension.

This is an optional extension to the activity.

Create a variable above the `for` loop named `Counter`
and set it equal to zero. Then, every time a new row
is read within the `for` loop, add a value of 1 to
this variable.
"""

# @TODO: Add a row counter to the CSV data.
# YOUR CODE HERE!
