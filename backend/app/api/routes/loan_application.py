from fastapi import APIRouter
from app.api.schemas import BalanceSheetResponseDTO, BalanceSheetRequestDTO

router = APIRouter(
    prefix="/loan-application"
)

@router.get("/initiate")
async def initialize():
    pass

# @router.post("/balance-sheet", response_model=BalanceSheetResponseDTO)
@router.post("/balance-sheet")
async def get_balance_sheet(request: BalanceSheetRequestDTO):
    pass

@router.post("/submit")
async def submit():
    pass