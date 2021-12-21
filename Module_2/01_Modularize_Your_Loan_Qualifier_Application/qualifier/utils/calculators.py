# As a lender,
# I want to calculate the monthly debt-to-income ratio
# so that we can assess the ability to pay of the borrower
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio


# As a lender,
# I want to calculate the loan-to-value ratio
# so that we can evaluate the risk of lending money to the borrower
def calculate_loan_to_value_ratio(loan_amount, home_value):
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio