# app/models.py
from sqlalchemy import Column, Integer, String
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    item = Column(String)
    status = Column(String, default="pending")
