# tests/test_todos_api.py
import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from apiTest import app

@pytest.mark.anyio
async def test_todo_crud_flow():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            r = await ac.post("/api/todos/", json={"title": "Read docs"})
            assert r.status_code == 201
            tid = r.json()["id"]

            r = await ac.get("/api/todos/?search=Read")
            assert r.status_code == 200 and r.json()["count"] >= 1

            r = await ac.patch(f"/api/todos/{tid}", json={"is_done": True})
            assert r.status_code == 200 and r.json()["is_done"] is True

            r = await ac.delete(f"/api/todos/{tid}")
            assert r.status_code == 204
