from fastapi import APIRouter
from app.api.schemas import *
from app.adapters import AccountingAdapterFactory
from app.common.enums import ACCOUNTING_SOFTWARE
from app.services import calculate_loan_approval

router = APIRouter(
    prefix="/loan-application"
)

@router.get("/accounting-services", response_model = list[str])
async def get_accounting_services():
    return [e.value for e in ACCOUNTING_SOFTWARE]

@router.post("/balance-sheet", response_model=list[BalanceSheetResponseDTO])
async def get_balance_sheet(request: BalanceSheetRequestDTO):
    adapter = AccountingAdapterFactory.create_adapter(request.accountingSoftware.value)
    normalized_balance_sheet = adapter.normalize_balance_sheet(adapter.fetch_balance_sheet(None, None))
    return normalized_balance_sheet

@router.post("/submit", response_model=LoanApplicationResponseDTO)
async def submit(request: LoanApplicationRequestDTO):
    adapter = AccountingAdapterFactory.create_adapter(request.accountingSoftware.value)
    normalized_balance_sheet = adapter.normalize_balance_sheet(adapter.fetch_balance_sheet(None, None))
    rate, amount = calculate_loan_approval(normalized_balance_sheet, request.loanAmount)
    return {"loanApprovalRate": rate, "loanAmountApproved": amount}