# app/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from app import models, schemas
import httpx
from loguru import logger

# inside create_order
@router.post("/orders", response_model=OrderRead)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Creating order for: {order.customer_name}")
    db_order = Order(customer_name=order.customer_name, item=order.item)
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)

    # Simulate external call
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("https://httpbin.org/post", json={"order_id": db_order.id})
            response.raise_for_status()
            logger.info("Notified external service successfully")
    except httpx.HTTPError as e:
        logger.error(f"Failed to notify shipping service: {e}")
        raise HTTPException(status_code=500, detail="External service failed")

    return db_order

async def get_orders(db: AsyncSession):
    result = await db.execute(select(models.Order))
    return result.scalars().all()

async def delete_order(db: AsyncSession, order_id: int):
    await db.execute(delete(models.Order).where(models.Order.id == order_id))
    await db.commit()
