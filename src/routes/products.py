from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas import products
from .. import models
from src.database import add
from typing import List

prod = APIRouter(
    tags=['Product'],
    prefix='/products'
)


@prod.get('/all', response_model=List[products.Product])
async def productsAll(db: Session = Depends(get_db)):
    product = db.query(models.Product).all()
    return product


@prod.get('/{id}', response_model=products.Product)
async def getProduct(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Product with this id {id} is not found')
    return product


@prod.post('/add')
async def addProducts(request: products.Product, db: Session = Depends(get_db)):
    newProduct = models.Product(productName=request.productName,
                                group=request.group,
                                description=request.description,
                                photoCode=request.photoCode,
                                amountInStock=request.amountInStock,
                                price=request.price)

    add(newProduct, db)
    return {'Message': 'Success'}


@prod.put('/{id}')
def editProduct(id: int, request: products.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Product with this id {id} not found')

    product.update(request.dict())
    db.commit()
    return 'Done'
