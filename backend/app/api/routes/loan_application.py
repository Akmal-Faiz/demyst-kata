from fastapi import APIRouter
from app.api.schemas import BalanceSheetResponseDTO, BalanceSheetRequestDTO
from app.adapters import AccountingAdapterFactory
from typing import List

router = APIRouter(
    prefix="/loan-application"
)

@router.get("/initiate")
async def initialize():
    pass

@router.post("/balance-sheet", response_model=List[BalanceSheetResponseDTO])
async def get_balance_sheet(request: BalanceSheetRequestDTO):
    adapter = AccountingAdapterFactory.create_adapter(request.accounting_software.value)
    normalized_balance_sheet = adapter.normalize_balance_sheet(adapter.fetch_balance_sheet(None, None))
    return normalized_balance_sheet

@router.post("/submit")
async def submit():
    pass