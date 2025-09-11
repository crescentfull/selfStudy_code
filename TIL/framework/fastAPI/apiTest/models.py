# models.py
from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, min_length=2, max_length=200)
    is_done: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

# 응답/요청 전용 스키마
class TodoCreate(SQLModel):
    title: str = Field(min_length=2, max_length=200)

class TodoUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=2, max_length=200)
    is_done: Optional[bool] = None

class TodoRead(SQLModel):
    id: int
    title: str
    is_done: bool
    created_at: datetime
    updated_at: datetime

class TodoList(SQLModel):
    count: int
    items: List[TodoRead]
