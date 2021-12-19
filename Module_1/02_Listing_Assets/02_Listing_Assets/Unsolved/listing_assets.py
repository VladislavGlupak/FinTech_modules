"""Listing Assets."""

# 1. @TODO: Use the following list, or copy this list to your new python script
bank_loans = [200, 500, 900, 100, 400, 800, 100]

# 2. @TODO: Create a variable called `number_of_loans`,
# declaring its value to be the length of the list of `bank_loans`.
# YOUR CODE HERE!
number_of_loans = len(bank_loans)
print(f"There are {number_of_loans} number of loans.")

# 3. @TODO: Create a variable called `largest_loan_amount’
# make it equal to the maximum value from the list of `bank_loans`.
# YOUR CODE HERE!
largest_loan_amount = max(bank_loans)

# 4. @TODO: Print the largest loan amount.
# YOUR CODE HERE!
print(largest_loan_amount)
