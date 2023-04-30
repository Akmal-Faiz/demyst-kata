from pydantic import BaseModel

class ProfitSummary(BaseModel):
    year: int
    profit: int

class DecisionEngineDTO(BaseModel):
    businessName: str
    yearEstablished: int
    profitSummary: list[ProfitSummary]
    preAssessmentValue: int