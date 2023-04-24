from pydantic import BaseModel, Field
from app.common.enums import ACCOUNTING_SOFTWARE
from typing import List, Literal

class BalanceSheetResponseDTO(BaseModel):
    # year: int
    # month: int = Field(..., ge=1, le=12)
    # profitOrLoss: float
    # assetsValue: float
    pass
    
class BalanceSheetRequestDTO(BaseModel):
    # business_details: BusinessDetails
    accounting_software: ACCOUNTING_SOFTWARE