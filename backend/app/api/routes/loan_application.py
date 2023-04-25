from fastapi import APIRouter
from app.api.schemas import BalanceSheetResponseDTO, BalanceSheetRequestDTO
from app.adapters import AccountingAdapterFactory

router = APIRouter(
    prefix="/loan-application"
)

@router.get("/initiate")
async def initialize():
    pass

# @router.post("/balance-sheet", response_model=BalanceSheetResponseDTO)
@router.post("/balance-sheet")
async def get_balance_sheet(request: BalanceSheetRequestDTO):
    adapter = AccountingAdapterFactory.create_adapter(request.accounting_software.value)
    return 

@router.post("/submit")
async def submit():
    pass