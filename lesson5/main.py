from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates

import logging

from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
templates = Jinja2Templates(directory="./lesson5/templates")
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# main_01
# @app.get("/")
# async def read_root():
#     logger.info('Finished GET')
#     return {'Hello': 'World'}

# main_02
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    logger.info(f'Received request for item_id: {item_id} with query: {q}')
    return {"item_id": item_id, "q": q}

# main_04 POST
# @app.post("/items")
# async def create_item(item: Item):
#     logger.info('Finished POST')
#     return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Finished PUT for item_id: {item_id}')
    return {'item_id': item_id, 'item': item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f'Finished DELETE for item_id: {item_id}')
    return {'item_id': item_id}

#main_09
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    logger.info(f'Received request for item_id: {item_id} with query: {q}')
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.get("/users/{user_id}/orders/{order_id}")
async def read_data(user_id: int, order_id: int):
    logger.info(f'Received request for order_id: {order_id}')
    return {'user_id': user_id, 'order_id': order_id}

@app.get("/items/")
async def strip_limit(skip: int = 0, limit: int =10):
    return {'skip': skip, 'limit': limit}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"
@app.get("/message")
async def read_message():
    message = {'message': 'Hello World'}
    return JSONResponse(content=message, status_code=200)

@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    logger.info(f'Received request for name: {name}')
    print(request)
    return templates.TemplateResponse("item.html", {"request": request, "name": name})