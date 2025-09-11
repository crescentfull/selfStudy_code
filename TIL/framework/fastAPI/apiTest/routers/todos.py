# routers/todos.py
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, func
from sqlmodel import Session
from datetime import datetime

from db import get_session
from models import Todo, TodoCreate, TodoRead, TodoUpdate, TodoList

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=TodoList)
def list_todos(
    search: Optional[str] = Query(None, description="제목 검색"),
    is_done: Optional[bool] = Query(None, description="완료 여부"),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    session: Session = Depends(get_session),
):
    filt = []
    if search:
        filt.append(Todo.title.ilike(f"%{search}%"))
    if is_done is not None:
        filt.append(Todo.is_done == is_done)

    base = select(Todo).where(*filt).order_by(Todo.created_at.desc())
    items = session.exec(base.offset(offset).limit(limit)).all()
    total = session.exec(select(func.count()).select_from(select(Todo).where(*filt).subquery())).one()
    return {"count": total, "items": items}

@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate, session: Session = Depends(get_session)):
    todo = Todo(title=payload.title)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.get("/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    return todo

@router.patch("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, payload: TodoUpdate, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(todo, k, v)
    todo.updated_at = datetime.utcnow()

    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(todo)
    session.commit()
