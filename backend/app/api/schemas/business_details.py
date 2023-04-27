from pydantic import BaseModel

class BusinessDetails(BaseModel):
    business_name: str
    year_established: int