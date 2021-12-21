# Initial imports
from pathlib import Path
from qualifier.utils.calculators import (calculate_monthly_debt_ratio, calculate_loan_to_value_ratio)
from qualifier.utils.fileio import load_csv

# This function loads a CSV file with the list of banks and available loans information
# from the file defined in `file_path`
def load_bank_data(file_path):
    csvpath = Path(file_path)
    return load_csv(csvpath)

# @TODO Define a function that implements the following user story:
# As a lender,
# I want to filter the bank list by checking the customer's desired loan against the bank's maximum loan size
# so that we can know which banks offer the loan amount requested by the customer
def filter_max_loan_size(loan_amount, bank_list):
    max_loans = []

    for loan in bank_list:
        if loan_amount <= int(loan[1]):
            max_loans.append(loan)
    return max_loans

# @TODO Define a function that implements the following user story:
# As a lender,
# I want to filter the bank list by checking if the customer's credit score is equal to or greater than the minimum allowed credit score defined by the bank
# so that we can know which banks are willing to offer a loan to the customer
def filter_credit_score(credit_score, bank_list):
    valid_credit_score = []

    for loan in bank_list:
        if credit_score >= int(loan[4]):
            valid_credit_score.append(loan)
    return valid_credit_score

# @TODO Define a function that implements the following user story:
# As a lender,
# I want to filter the bank list by comparing if the customer's debt-to-income is equal to or less than the maximum debt-to-income ratio allowed by the bank
# so that we can assess if the customer will have payment capacity according to the bank's criteria
def filter_debt_to_income(monthly_debt_ratio, bank_list):
    good_dti = []

    for loan in bank_list:
        if monthly_debt_ratio <= float(loan[3]):
            good_dti.append(loan)
    return good_dti


# @TODO Define a function that implements the following user story:
# As a lender,
# I want to filter the bank list by checking if the customer's loan-to-value is equal to or less than the maximum loan-to-value ratio allowed by the bank
# so that we assess if the customer's home value is worth as an asset to secure the loan
def filter_loan_to_value(loan_to_value_ratio, bank_list):
    good_ltv = []

    for loan in bank_list:
        if loan_to_value_ratio <= float(loan[2]):
            good_ltv.append(loan)
    return good_ltv


# This function implements the following user story:
# As a customer,
# I want to know what are the best loans in the market according to my financial profile
# so that I can choose the best option according to my needs
def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


# This function is the main execution point of the application. It triggers all the business logic.
def run():
    # Set the file path of the CVS file with the banks and loans information
    file_path = Path("./data/daily_rate_sheet.csv")
    # Load the latest Bank data
    bank_data = load_bank_data(file_path)

    # This print statement will display all of the bank data that is provided.
    # print(f"bank_data: {bank_data}")

    # The following lines, set the applicant's information and implements the following user story:
    # As a customer,
    # I want to provide my financial information
    # so that I can apply for a loan
    credit_score = 750
    debt = 5000
    income = 20000
    loan_amount = 100000
    home_value = 210000

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Print the list of qualifying loans
    print(qualifying_loans)


run()
