from app.services.preassessment import RuleEngine
re = RuleEngine()

def calculate_loan_approval(balance_sheet, loanAmount):
    rate = re.evaluate(balance_sheet, loanAmount)
    amount = loanAmount * rate /100
    return rate, amount