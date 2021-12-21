# module filters banks by credit score
def filter_credit_score(credit_score, bank_list):
    credit_score_approval_list = []
    for bank in bank_list:
        if credit_score >= int(bank[4]):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list