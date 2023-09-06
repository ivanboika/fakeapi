from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas import cartItem


carts = APIRouter(
    prefix='/cart',
    tags=['Cart', 'Producs']
)


@carts.get('/{cartID}', response_model=cartItem)
async def getCart(cartID: int, db: Session = Depends(get_db)):
    pass
