from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db, add
from src.schemas import user
from .. import models
from .. import hashing

reg = APIRouter(
    tags=['Registration', 'User'],
    prefix='/reg'
)


@reg.post('/')
async def regUser(request: user.User, db: Session = Depends(get_db)):
    checkUser = db.query(models.User).filter(models.User.username == request.username)
    if checkUser.first():
        raise HTTPException(status_code=status.HTTP_302_FOUND,
                            detail=f'User with chosen username({request.username} exists)')
    newUser = models.User(username=request.username,
                          password=hashing.Hash.bcrypt(request.hashedPassword),
                          companyName=request.companyName,
                          stateCadastrCode=request.stateCadastrCode,
                          legalAddress=request.legalAddress,
                          companyRating=request.companyRating)
    add(newUser, db)
    return {'Message': 'Successfully registered'}
