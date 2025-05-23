# app/schemas.py
from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str
    item: str

class OrderOut(OrderCreate):
    id: int
    status: str

    class Config:
        orm_mode = True
