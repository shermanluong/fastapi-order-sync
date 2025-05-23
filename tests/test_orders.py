# tests/test_orders.py
import pytest
from httpx import AsyncClient
from app.main import app
from app.database import init_db

@pytest.fixture(scope="module", autouse=True)
async def setup_db():
    await init_db()  # Ensure tables are created before running tests

@pytest.mark.asyncio
async def test_create_order():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/orders", json={"customer_name": "Bob", "item": "Test Widget"})
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Bob"
    assert data["item"] == "Test Widget"

@pytest.mark.asyncio
async def test_list_orders():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_order_triggers_external_api():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/orders", json={"customer_name": "Alice", "item": "External Widget"})
    assert response.status_code == 200
    assert response.json()["item"] == "External Widget"
