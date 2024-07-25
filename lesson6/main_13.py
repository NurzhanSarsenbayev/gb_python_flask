from typing import List

from pydantic import BaseModel, Field
import databases
import sqlalchemy
from fastapi import FastAPI
from sqlalchemy.sql.functions import user

DATABASE_URL = "sqlite:///test_fastapi.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


metadata.create_all(engine)
app = FastAPI()

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)

# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(id=i, name=f"User {i}", email=f"mail{i}@mail.ru")
#         await database.execute(query)
#     return {'message': f'{count} fake users created!'}

@app.post("/users", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    query = user.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}

@app.get("/users", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@app.get("/users/{id}", response_model=User)
async def read_user(id: int):
    query = users.select().where(users.c.id == id)
    return await database.fetch_one(query)

@app.put("/users/{id}", response_model=User)
async def update_user(id: int, user: UserIn):
    query = users.update().where(users.c.id == id).values(name=user.name, email=user.email)
    await database.execute(query)
    return {**user.dict(), "id": id}

@app.delete('/users/{id}')
async def delete_user(id: int):
    query = users.delete().where(users.c.id == id)
    await database.execute(query)
    return {**user.dict(), "id": id}