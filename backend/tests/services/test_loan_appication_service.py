from app.services.loan_application_service import get_profit_summary
from .balance_sheet_test_data import *

def test_get_profit_summary():
    balance_sheet = BALANCE_SHEET_1
    expected_outcome = YEARLY_PROFIT_SUMMARY
    assert get_profit_summary(balance_sheet) == expected_outcome
    