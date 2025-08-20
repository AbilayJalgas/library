from fastapi import APIRouter
from database.borrowservice import borrow_book_db, return_book_db

borrow_router = APIRouter(prefix="/borrow", tags=["Borrow API"])

@borrow_router.get("/borrow_book")
async def borrow_book_api(book_id: int, user_id: int):
    info = borrow_book_db(book_id=book_id, user_id=user_id)

    return {"status": 1, "message": info}


@borrow_router.post("/return_book")
async def return_book_api(book_id: int, user_id: int):
    info = return_book_db(book_id=book_id, user_id=user_id)

    return {"status": 1, "message": info}