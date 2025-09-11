# app.py
from fastapi import FastAPI
from db import init_db
from routers.todos import router as todos_router

app = FastAPI(title="RESTLab API (FastAPI)")
app.include_router(todos_router, prefix="/api")

@app.on_event("startup")
def on_startup():
    init_db()
