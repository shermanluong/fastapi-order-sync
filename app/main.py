# app/main.py
from fastapi import FastAPI
from app import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.init_db()

@app.get("/")
async def root():
    return {"message": "FastAPI Order Sync is running"}