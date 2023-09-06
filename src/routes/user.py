from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas import user
from .. import models


userRoute = APIRouter(
    prefix='/user',
    tags=['User']
)


@userRoute.get('/{login}', response_model=user.User)
async def getUser(login: str, db: Session = Depends(get_db)):
    checkUser = db.query(models.User).filter(models.User.username == login).first()
    if not checkUser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f'User with login {login} is not found')
    return checkUser
