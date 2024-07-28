# Задание
#
# Объедините студентов в команды по 2-5 человек в сессионных залах.
#
# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
#
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.
# Create Read Update Delete

from typing import List

import sqlalchemy
from databases import Database
from fastapi import FastAPI, Depends
from homework6.models import DATABASE_URL, metadata
from homework6.schemas import User, UserIn, Item, ItemIn, Order, OrderIn, OrderStatus
from homework6.crud.item import create_item, read_item, read_items, update_item, delete_item
from homework6.crud.user import create_user, read_user, read_users, update_user, delete_user
from homework6.crud.order import create_order, read_order, read_orders, update_order, delete_order


database = Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/items/", response_model=Item)
async def create_item_endpoint(item: ItemIn):
    return await create_item(database, item)

@app.get("/items/", response_model=List[Item])
async def read_items_endpoint():
    return await read_items(database)

@app.get("/items/{item_id}", response_model=Item)
async def read_item_endpoint(item_id: int):
    return await read_item(database, item_id)

@app.put("/items/{item_id}", response_model=Item)
async def update_item_endpoint(item_id: int, item: ItemIn):
    return await update_item(database, item_id, item)
@app.delete("/items/{item_id}")
async def delete_item_endpoint(item_id: int):
    return await delete_item(database, item_id)

@app.post("/users/", response_model=User)
async def create_user_endpoint(user: UserIn):
    return await create_user(database, user)
@app.get("/users/", response_model=List[User])
async def read_users_endpoint():
    return await read_users(database)
@app.get("/users/{user_id}", response_model=User)
async def read_user_endpoint(user_id: int):
    return await read_user(database, user_id)
@app.put("/users/{user_id}", response_model=User)
async def update_user_endpoint(user_id: int, user: UserIn):
    return await update_user(database, user_id, user)
@app.delete("/users/{user_id}")
async def delete_user_endpoint(user_id: int):
    return await delete_user(database, user_id)

@app.post("/orders/", response_model=Order)
async def create_order_endpoint(order: OrderIn):
    return await create_order(database, order)
@app.get("/orders/", response_model=List[Order])
async def read_orders_endpoint():
    return await read_orders(database)
@app.get("/orders/{order_id}", response_model=Order)
async def read_order_endpoint(order_id: int):
    return await read_order(database, order_id)
@app.put("/orders/{order_id}", response_model=Order)
async def update_order_endpoint(order_id: int, order: OrderStatus):
    return await update_order(database, order_id, order)
@app.delete("/orders/{order_id}")
async def delete_order_endpoint(order_id: int):
    return await delete_order(database, order_id)

# DATABASE_URL = "sqlite:///homework_6.db"
# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()
#
# items = sqlalchemy.Table(
#     'items',
#     metadata,
#     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column('name', sqlalchemy.String),
#     sqlalchemy.Column('description', sqlalchemy.String),
#     sqlalchemy.Column('price', sqlalchemy.Integer),
# )
# users = sqlalchemy.Table(
#     'users',
#     metadata,
#     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column('name', sqlalchemy.String),
#     sqlalchemy.Column('last_name', sqlalchemy.String),
#     sqlalchemy.Column('email', sqlalchemy.String),
#     sqlalchemy.Column('password', sqlalchemy.String),
# )
# orders = sqlalchemy.Table(
#     'orders',
#     metadata,
#     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
#     sqlalchemy.Column('item_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('items.id')),
#     sqlalchemy.Column('date', sqlalchemy.DateTime),
#     sqlalchemy.Column('status', sqlalchemy.BOOLEAN)
# )
# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)
#
# app = FastAPI()


# class User(BaseModel):
#     id: int
#     name: str
#     last_name: str
#     email: EmailStr
#     password: str
#
#
# class UserIn(BaseModel):
#     name: str
#     last_name: str
#     email: EmailStr
#     password: str
#
#
# class Item(BaseModel):
#     id: int
#     name: str
#     description: str
#     price: int
#
#
# class ItemIn(BaseModel):
#     name: str
#     description: str
#     price: int
#
#
# class Order(BaseModel):
#     id: int
#     user_id: int
#     item_id: int
#     date: datetime
#     status: bool= Field(default=False,)
# class OrderIn(BaseModel):
#     user_id: int
#     item_id: int
#     date: datetime
#     status: bool = Field(default=False, )
# class OrderStatus(BaseModel):
#     status: bool

# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

# @app.post("/items/", response_model=Item)
# async def create_item(item: ItemIn):
#     query = items.insert().values(**item.dict())
#     last_record_id = await database.execute(query)
#     return {**item.dict(), "id": last_record_id}
#
#
# @app.get("/items/", response_model=List[Item])
# async def read_items():
#     query = items.select()
#     return await database.fetch_all(query)
#
#
# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: int):
#     query = items.select().where(items.c.id == item_id)
#     item = await database.fetch_one(query)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item
#
#
# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: int, item: ItemIn):
#     query = items.update().where(items.c.id == item_id).values(**item.dict())
#     if query is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     await database.execute(query)
#     return {**item.dict(), "id": item_id}
#
#
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     query = items.select().where(items.c.id == item_id)
#     item = await database.fetch_one(query)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     delete_query = items.delete().where(items.c.id == item_id)
#     await database.execute(delete_query)


# @app.post("/users/", response_model=User)
# async def create_user(user: UserIn):
#     query = users.insert().values(**user.dict())
#     last_record_id = await database.execute(query)
#     return {**user.dict(), "id": last_record_id}
#
#
# @app.get("/users/", response_model=List[User])
# async def read_users():
#     query = users.select()
#     return await database.fetch_all(query)
#
#
# @app.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int):
#     query = users.select().where(users.c.id == user_id)
#     user = await database.fetch_one(query)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#
#
# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, user: UserIn):
#     query = users.update().where(users.c.id == user_id).values(**user.dict())
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     await database.execute(query)
#     return {**user.dict(), "id": user_id}
#
#
# @app.delete("/users/")
# async def delete_user(user_id: int):
#     query = users.select().where(users.c.id == user_id)
#     user = await database.fetch_one(query)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     delete_query = users.delete().where(users.c.id == user_id)
#     await database.execute(delete_query)
#     return user


# @app.post("/orders/", response_model=Order)
# async def create_order(order: OrderIn):
#     user_query = users.select().where(users.c.id == order.user_id)
#     user = await database.fetch_one(user_query)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#
#     item_query = items.select().where(items.c.id == order.item_id)
#     item = await database.fetch_one(item_query)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#
#     query = orders.insert().values(**order.dict())
#     last_record_id = await database.execute(query)
#     return {**order.dict(), "id": last_record_id}
#
#
# @app.get('/orders/', response_model=List[Order])
# async def read_orders():
#     query = orders.select()
#     return await database.fetch_all(query)
#
#
# @app.get('/orders/{order_id}', response_model=Order)
# async def read_order(order_id: int):
#     query = orders.select().where(orders.c.id == order_id)
#     order = await database.fetch_one(query)
#     if order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# @app.put('/orders/{order_id}', response_model=Order)
# async def update_order(order_id: int, order: OrderStatus):
#     query = orders.update().where(orders.c.id == order_id).values(**order.dict())
#     await database.execute(query)
#     order = await database.fetch_one(orders.select().where(orders.c.id == order_id))
#     return order
#
#
# @app.delete('/orders/{order_id}')
# async def delete_order(order_id: int):
#     query = orders.select().where(orders.c.id == order_id)
#     order = await database.fetch_one(query)
#     if order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     delete_query = orders.delete().where(orders.c.id == order_id)
#     await database.execute(delete_query)
#     return order
