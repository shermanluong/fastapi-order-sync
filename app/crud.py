# app/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from app import models, schemas

async def create_order(db: AsyncSession, order: schemas.OrderCreate) -> models.Order:
    db_order = models.Order(**order.dict())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

async def get_orders(db: AsyncSession):
    result = await db.execute(select(models.Order))
    return result.scalars().all()

async def delete_order(db: AsyncSession, order_id: int):
    await db.execute(delete(models.Order).where(models.Order.id == order_id))
    await db.commit()
