from database import get_db
from database.models import User


# Функция для создания пользователя
def create_user_db(username, password, role):
    db = next(get_db())

    new_user = User(username=username, password=password, role=role)
    db.add(new_user)
    db.commit()
    return "Пользователь успешно добавлен"

# Функция для получения всех пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()
    return all_users

# Функция для получения конкретного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).sorted_by(id=user_id).first()
    if exact_user:
        return exact_user
    return False

# Удаление пользователя
def delete_user_db(user_id):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)
    if exact_user:
        db.delete(exact_user)
        db.commit()
        return "Пользователь успешно удален"
    return False