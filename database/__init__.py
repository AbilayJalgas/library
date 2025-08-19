from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Указываем тип БД
SQL_DATABASE = "sqlite:///library.db"

# Создаем движок
engine = create_engine(SQL_DATABASE)

# Создаем сессию что-бы хранить данные
SessionLocal = sessionmaker(bind=engine)

# Создаем полноценную базу
Base = declarative_base()

# Функция для подключения к БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
        