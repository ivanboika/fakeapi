from pydantic import BaseModel


class CartItem(BaseModel):
    productId: int
    quantity: int

    class Config:
        orm_mode = True