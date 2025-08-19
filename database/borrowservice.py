from database import get_db
from database.models import Borrow, Book
from datetime import datetime


# Взять книгу
def borrow_book_db(book_id, user_id):
    db = next(get_db())

    book = db.query(Book).filter_by(id=book_id, available=True).first()
    if not book:
        return "Книга не доступна"
    borrow = Borrow(user_id=user_id, book_id=book_id)
    book.available = False
    db.add(borrow)
    db.commit()
    return f"{book.title} взят в аренду"

# Вернуть книгу
def return_book_db(book_id, user_id):
    db = next(get_db())

    borrow = db.query(Borrow).filter_by(user_id=user_id, book_id=book_id, return_date=None).first()
    if not borrow:
        return "Вы не брали такую книгу"
    borrow.return_date = datetime.utcnow()
    book = db.query(Book).filter_by(id=book_id).first()
    book.available = True
    db.commit()
    return f"Вы вернули книгу {book.title}"