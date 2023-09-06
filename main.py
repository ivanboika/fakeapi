from fastapi import FastAPI
from src.routes import auth, products, registr, user
from src.database import engine
from src import models

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(products.prod)
app.include_router(registr.reg)
app.include_router(user.userRoute)
