# app/main.py (add below root endpoint)
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, database

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
async def get_db():
    async with database.SessionLocal() as session:
        yield session

@app.post("/orders", response_model=schemas.OrderOut)
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_order(db, order)

@app.get("/orders", response_model=list[schemas.OrderOut])
async def list_orders(db: AsyncSession = Depends(get_db)):
    return await crud.get_orders(db)

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    await crud.delete_order(db, order_id)
    return {"message": f"Order {order_id} deleted"}
