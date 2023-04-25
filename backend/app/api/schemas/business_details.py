from pydantic import BaseModel, Field
from typing import Optional

class BusinessDetails(BaseModel):
    name: str
    year_established: int