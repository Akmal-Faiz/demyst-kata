from fastapi import APIRouter
from app.api.schemas import BalanceSheetResponseDTO, BalanceSheetRequestDTO
from app.adapters import AccountingAdapterFactory
from app.common.enums import ACCOUNTING_SOFTWARE

router = APIRouter(
    prefix="/loan-application"
)

@router.get("/accounting-services", response_model = list[str])
async def get_accounting_services():
    # raise TypeError
    return [e.value for e in ACCOUNTING_SOFTWARE]

@router.post("/balance-sheet", response_model=list[BalanceSheetResponseDTO])
async def get_balance_sheet(request: BalanceSheetRequestDTO):
    adapter = AccountingAdapterFactory.create_adapter(request.accounting_software.value)
    normalized_balance_sheet = adapter.normalize_balance_sheet(adapter.fetch_balance_sheet(None, None))
    return normalized_balance_sheet

@router.post("/submit")
async def submit():
    pass