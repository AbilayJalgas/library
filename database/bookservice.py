from database import get_db
from database.models import Book


# Функция для добавления книги
def add_book_db(title, author, year, available, genre, role):
    db = next(get_db())

    add_book = Book(title=title, author=author, year=year, available=available, genre=genre)
    if not role['can_add_book']:
        return "Только админ может добавлять книги"
    db.add(add_book)
    db.commit()
    return "Книга успешно добавлена"

# Функция для удаления книги
def delete_book_db(book_id, role):
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
def get_all_book_db():
    db = next(get_db())

    all_book = db.query(Book).all()
    return all_book


def get_exact_book_db(book_id):
    db = next(get_db())

    exact_book = db.query(Book).filter_by(id=book_id).first()
    if exact_book:
        return exact_book
    return False

# Функция для редактирования книги
def update_book_db(book_id, change_info, new_info, role):
    db = next(get_db())

    exact_book = db.query(Book).filter_by(id=book_id).first()
    if exact_book:
        if not role["can_update_book"]:
            return "У вас нет доступа изменять книги"
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
