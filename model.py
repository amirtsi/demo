from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Order(BaseModel):
    id: int
    items: List[Item]
    user: User
    total_amount: float
    shipping_address: Optional[str] = None


class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True
