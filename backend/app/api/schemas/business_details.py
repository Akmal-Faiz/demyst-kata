from pydantic import BaseModel

class BusinessDetails(BaseModel):
    businessName: str
    yearEstablished: int