from app.services.preassessment.rule_engine import RuleEngine

def calculate_loan_approval(balance_sheet, loanAmount):
    re = RuleEngine()
    rate = re.evaluate(balance_sheet, loanAmount)
    amount = loanAmount * rate /100
    return rate, amount