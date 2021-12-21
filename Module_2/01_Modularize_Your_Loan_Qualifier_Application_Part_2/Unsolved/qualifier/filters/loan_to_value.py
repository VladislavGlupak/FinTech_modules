# module filters banks by LTV

def filter_loan_to_value(loan_to_value_ratio, bank_list):
    loan_to_value_approval_list = []

    for bank in bank_list:
        if loan_to_value_ratio <= float(bank[2]):
            loan_to_value_approval_list.append(bank)
    return loan_to_value_approval_list