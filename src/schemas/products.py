from pydantic import BaseModel


class Product(BaseModel):
    productName: str
    group: str
    description: str
    amountInStock: int
    price: float

    class Config:
        orm_mode = True
