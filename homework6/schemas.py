from pydantic import BaseModel,EmailStr,Field
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr
    password: str


class UserIn(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int


class ItemIn(BaseModel):
    name: str
    description: str
    price: int


class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    date: datetime
    status: bool= Field(default=False,)
class OrderIn(BaseModel):
    user_id: int
    item_id: int
    date: datetime
    status: bool = Field(default=False, )
class OrderStatus(BaseModel):
    status: bool