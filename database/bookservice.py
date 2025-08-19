from database import get_db
from database.models import Book
from fastapi import Depends, HTTPException




roles = {
    "admin": {"can_add_book": True, "can_delete_book": True},
    "user": {"can_add_book": False, "can_delete_book": False}
}

def get_current_role(role: str):
    if role not in roles:
        raise HTTPException(status_code=403, detail="Нет доступа")
    return roles[role]

# Функция для добавления книги
def add_book_db(title, author, year, available, gener, role=Depends(get_current_role)):
    db = next(get_db())

    add_book = Book(title=title, author=author, year=year, available=available, gener=gener)
    if not role['can_add_book']:
        return "Только админ может добавлять книги"
    db.add(add_book)
    db.commit()
    return "Книга успешно добавлена"

# Функция для удаления книги
def delete_book_db(book_id, role=Depends(get_current_role)):
    db = next(get_db())

    book = db.query(Book).filter_by(id=book_id).first()
    if book:
        if not role['can_delete_book']:
            return "Только админ может удалять книги"
        db.delete(book)
        db.commit()
        return "Книга успешна удалена"
    return False

# Функция для получения конкретной или всех книг
def get_all_or_exact_book_db(book_id):
    db = next(get_db())

    exact_book = db.query(Book).filter_by(id=book_id).first()
    if exact_book:
        return exact_book
    else:
        return db.query(Book).all()

# Функция для редактирования книги
def update_book_db(book_id, change_info, new_info):
    db = next(get_db())

    exact_book = db.query(Book).filter_by(book_id).first()
    if exact_book:
        if change_info == "title":
            exact_book.title = new_info
        elif change_info == "author":
            exact_book.author = new_info
        elif change_info == "year":
            exact_book.year = new_info
        elif change_info == "available":
            exact_book.available = new_info
        elif change_info == "genre":
            exact_book.genre = new_info
        db.commit()
        return True
    return False
