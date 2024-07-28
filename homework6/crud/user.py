from sqlalchemy import insert, select, update, delete
from fastapi import HTTPException
from databases import Database
from homework6.models import users
from homework6.schemas import UserIn
import bcrypt


async def create_user(database: Database, user: UserIn):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_data = user.dict()
    user_data['password'] = hashed_password.decode('utf-8')
    query = insert(users).values(**user_data)
    last_record_id = await database.execute(query)
    return {**user_data, "id": last_record_id}


async def read_users(database: Database):
    query = select(users)
    return await database.fetch_all(query)


async def read_user(database: Database, user_id: int):
    query = select(users).where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=400,
                            detail="User with provided ID not found. Please check your input and try again.")
    return user


async def update_user(database: Database, user_id: int, user: UserIn):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_data = user.dict()
    user_data['password'] = hashed_password.decode('utf-8')

    query = select(users).where(users.c.id == user_id)
    user_check = await database.fetch_one(query)
    if user_check is None:
        raise HTTPException(status_code=400,
                            detail="User with provided ID not found. Please check your input and try again.")

    update_query = update(users).where(users.c.id == user_id).values(**user_data)
    await database.execute(update_query)
    return {**user_data, "id": user_id,}


async def delete_user(database: Database, user_id: int):
    query = select(users).where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=400,
                            detail="User with provided ID not found. Please check your input and try again.")
    delete_query = delete(users).where(users.c.id == user_id)
    await database.execute(delete_query)
