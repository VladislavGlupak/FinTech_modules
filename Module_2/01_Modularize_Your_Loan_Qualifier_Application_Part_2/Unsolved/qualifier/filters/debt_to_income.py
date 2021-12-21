# module filters banks by MDR

def filter_debt_to_income(monthly_debt_ratio, bank_list):
    debit_to_income_approval_list = []
    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            debit_to_income_approval_list.append(bank)
    return debit_to_income_approval_list