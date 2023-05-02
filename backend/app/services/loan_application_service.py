from app.services.preassessment import RuleEngine
from app.adapters.decision_engine import DecisionEngineAdapter
from itertools import groupby

re = RuleEngine()
de = DecisionEngineAdapter()

def calculate_loan_approval(balance_sheet, loanAmount, businessDetails):
    preassessment_rate = re.evaluate(balance_sheet, loanAmount, businessDetails.businessName, businessDetails.yearEstablished)
    rate = de.get_decision({
        "businessName": businessDetails.businessName,
        "yearEstablished": businessDetails.yearEstablished,
        "profitSummary": get_profit_summary(balance_sheet),
        "preAssessmentValue": preassessment_rate
    })
    amount = loanAmount * rate /100
    return rate, amount

def get_profit_summary(balance_sheet):    
    yearly_profit_summary = []

    for year, data_in_year in groupby(balance_sheet, key=lambda item: item["year"]):
        total_profit = sum(item["profitOrLoss"] for item in data_in_year)
        yearly_profit_summary.append({"year": year, "profitSummary": total_profit})

    return yearly_profit_summary
