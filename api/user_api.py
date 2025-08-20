from fastapi import APIRouter
from database.userservice import create_user_db, get_exact_user_db, get_all_users_db, delete_user_db, update_user_db


user_router = APIRouter(prefix="/user", tags=["User API"])


@user_router.post("/create_user")
async def create_user_api(username: str, password: str, role: str):
    info = create_user_db(username=username, password=password, role=role)

    return {"status": 1, "message": info}


@user_router.get("/get_exact_user")
async def get_exact_user_api(user_id: int):
    info = get_exact_user_db(user_id)
    if info:
        return {"status": 1, "message": info}
    return {"status": 0, "message": "Нет такого пользователя"}


@user_router.get("/get_all_user")
async def get_all_user_api():
    info = get_all_users_db()

    return {"status": 1, "message": info}


@user_router.put("/update_user")
async def update_user_api(user_id: int, change_info: str, new_info: str):
    info = update_user_db(user_id, change_info=change_info, new_info=new_info)

    return {"status": 1, "message": info}


@user_router.delete("/delete_user")
async def delete_user_api(user_id):
    info = delete_user_db(user_id)

    if info:
        return {"status": 1, "message": info}
    return {"status": 0, "message": "Нет такого пользователя"}