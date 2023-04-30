from app.services.preassessment.rules import ProfitLastYearRule
from tests.services.balance_sheet_test_data import *

def test_profit_last_year_profit():
    rule = ProfitLastYearRule()
    balance_sheet = BALANCE_SHEET_1
    assert rule.evaluate(balance_sheet) == (True, 60)
    
def test_profit_last_year_loss():
    rule = ProfitLastYearRule()
    balance_sheet = BALANCE_SHEET_1
    for i in balance_sheet:
        i["profitOrLoss"] = 0
    assert rule.evaluate(balance_sheet) == (False, None)