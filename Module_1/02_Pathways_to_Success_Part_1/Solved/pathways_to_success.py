"""Pathways to Success."""
# Import the Path tool from the pathlib library
from pathlib import Path

# Create a path to the `quarterly_data.csv` file
csvpath = Path("quarterly_data.csv")

# Print the relative path (the relative location of the file)
print(f"The relative CSV path is {csvpath}")

# Print the absolute path (The absolute location of the file on the computer)
print(f"The absolute CSV path is {csvpath.absolute()}")
