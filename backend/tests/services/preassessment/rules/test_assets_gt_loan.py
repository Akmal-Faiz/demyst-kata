from app.services.preassessment.rules import AssetsGtLoanRule
from tests.services.balance_sheet_test_data import *

def test_assets_gt_loan_pass():
    rule = AssetsGtLoanRule()
    balance_sheet = BALANCE_SHEET_1
    loan_amount = float('-inf')
    
    assert rule.evaluate(balance_sheet, loan_amount) == (True, 100)
    
def test_assets_gt_loan_fail():
    rule = AssetsGtLoanRule()
    balance_sheet = BALANCE_SHEET_1
    loan_amount = float('inf')
    
    assert rule.evaluate(balance_sheet, loan_amount) == (False, None)