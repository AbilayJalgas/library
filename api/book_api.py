from fastapi import APIRouter, Depends, HTTPException
from database.bookservice import add_book_db, delete_book_db, get_all_book_db, get_exact_book_db, update_book_db

book_router = APIRouter(prefix="/book", tags=["Book API"])


roles = {
    "admin": {"can_add_book": True, "can_delete_book": True, "can_update_book": True},
    "user": {"can_add_book": False, "can_delete_book": False, "can_update_book": False}
}

def get_current_role(role: str):
    if role not in roles:
        raise HTTPException(status_code=403, detail="Нет доступа")
    return roles[role]

@book_router.post("/add_book")
async def add_book_api(title: str, author: str, year: str, genre: str, available: bool, role: dict=Depends(get_current_role)):
    info = add_book_db(title=title, author=author, year=year, genre=genre, available=available, role=role)

    return {"status": 1, "message": info}


@book_router.get("/get_all_books")
async def get_all_books_api():
    info = get_all_book_db()

    return {"status": 1, "message": info}


@book_router.get('/get_exact_book')
async def get_exact_book_api(book_id):
    info = get_exact_book_db(book_id)

    return {"status": 1, "message": info}


@book_router.put('/update_book')
async def update_book_api(book_id, change_info, new_info, role: dict=Depends(get_current_role)):
    info = update_book_db(book_id=book_id, change_info=change_info, new_info=new_info, role=role)

    return {"status": 1, "message": info}


@book_router.delete('/delete_book')
async def delete_book_api(book_id: int, role: dict=Depends(get_current_role)):
    info = delete_book_db(book_id=book_id, role=role)

    return {"status": 1, "message": info}