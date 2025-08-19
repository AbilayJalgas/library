from database import Base
from sqlalchemy import Enum, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import enum


class Role(enum.Enum):
    user = "user"
    admin = "admin"

# Создаем модель user
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16), nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), default=Role.user)


# Создаем библиотеку
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)


class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    borrow_date = Column(DateTime, default=datetime.utcnow())
    return_date = Column(DateTime, nullable=True)

    book_fk = relationship(Book, lazy="subquery")
    user_fk = relationship(User, lazy="subquery")
