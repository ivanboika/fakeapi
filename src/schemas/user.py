from pydantic import BaseModel


class User(BaseModel):
    username: str
    companyName: str
    stateCadastrCode: str
    legalAddress: str
    companyRating: float

    class Config:
        orm_mode = True
