from fastapi import FastAPI, HTTPException
from database import Base, engine
from api.user_api import user_router
from api.book_api import book_router
from api.borrow_api import borrow_router


app = FastAPI(docs_url="/")

Base.metadata.create_all(engine)

app.include_router(user_router)
app.include_router(book_router)
app.include_router(borrow_router)