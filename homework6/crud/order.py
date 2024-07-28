from sqlalchemy import insert, select, update, delete
from fastapi import HTTPException
from databases import Database
from homework6.models import orders, users, items
from homework6.schemas import OrderIn, OrderStatus


async def create_order(database: Database, order: OrderIn):
    user_query = select(users).where(users.c.id == order.user_id)
    user = await database.fetch_one(user_query)
    if user is None:
        raise HTTPException(status_code=400,
                            detail="User with provided ID not found. Please check your input and try again.")

    item_query = select(items).where(items.c.id == order.item_id)
    item = await database.fetch_one(item_query)
    if item is None:
        raise HTTPException(status_code=400,
                            detail="Item with provided ID not found. Please check your input and try again.")

    query = insert(orders).values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


async def read_orders(database: Database):
    query = select(orders)
    return await database.fetch_all(query)


async def read_order(database: Database, order_id: int):
    query = select(orders).where(orders.c.id == order_id)
    order = await database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=400,
                            detail="Order with provided ID not found. Please check your input and try again.")
    return order


async def update_order(database: Database, order_id: int, order: OrderStatus):
    query = select(orders).where(orders.c.id == order_id)
    order_check = await database.fetch_one(query)
    if order_check is None:
        raise HTTPException(status_code=400,
                            detail="Order with provided ID not found. Please check your input and try again.")
    existing_order = dict(order_check)
    updated_order_data = {**existing_order, **order.dict()}

    update_query = update(orders).where(orders.c.id == order_id).values(**updated_order_data)
    await database.execute(update_query)

    return {**updated_order_data, "id": order_id}


async def delete_order(database: Database, order_id: int):
    query = select(orders).where(orders.c.id == order_id)
    order = await database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=400,
                            detail="Order with provided ID not found. Please check your input and try again.")
    delete_query = delete(orders).where(orders.c.id == order_id)
    await database.execute(delete_query)
