from pydantic import BaseModel, Field
from app.common.enums import ACCOUNTING_SOFTWARE
from .business_details import BusinessDetails

class LoanApplicationResponseDTO(BaseModel):
    loanApprovalRate: int
    loanAmountApproved: float
    
class LoanApplicationRequestDTO(BaseModel):
    businessDetails: BusinessDetails
    loanAmount: float
    accountingSoftware: ACCOUNTING_SOFTWARE