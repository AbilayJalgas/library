from fastapi import FastAPI, HTTPException
from database import Base, engine
from api.user_api import user_router


app = FastAPI(docs_url="/")

Base.metadata.create_all(engine)

app.include_router(user_router)

