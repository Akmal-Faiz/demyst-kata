from pydantic import BaseModel

class ProfitSummary(BaseModel):
    year: int
    profit: int

class DecisionEngineDTO(BaseModel):
    business_name: str
    year_established: int
    profit_summary: list[ProfitSummary]
    preAssessment_value: int