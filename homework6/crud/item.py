from sqlalchemy import insert, select, update, delete
from fastapi import HTTPException
from databases import Database
from homework6.models import items
from homework6.schemas import ItemIn


async def create_item(database: Database, item: ItemIn):
    query = insert(items).values(**item.dict())
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


async def read_items(database: Database, ):
    query = select(items)
    return await database.fetch_all(query)


async def read_item(database: Database, item_id: int):
    query = select(items).where(items.c.id == item_id)
    item = await database.fetch_one(query)
    if item is None:
        raise HTTPException(status_code=400,
                            detail="Item with provided ID not found. Please check your input and try again.")
    return item


async def update_item(database: Database, item_id: int, item: ItemIn):
    query = select(items).where(items.c.id == item_id)
    item_check = await database.fetch_one(query)
    if item_check is None:
        raise HTTPException(status_code=400,
                            detail="Item with provided ID not found. Please check your input and try again.")
    update_query = update(items).where(items.c.id == item_id).values(**item.dict())
    await database.execute(update_query)
    return {**item.dict(), "id": item_id}


async def delete_item(database: Database, item_id: int):
    query = select(items).where(items.c.id == item_id)
    item = await database.fetch_one(query)
    if item is None:
        raise HTTPException(status_code=400,
                            detail="Item with provided ID not found. Please check your input and try again.")
    delete_query = delete(items).where(items.c.id == item_id)
    await database.execute(delete_query)
