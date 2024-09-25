from sqlmodel import SQLModel, Field
from typing import List
from pydantic import BaseModel


class TodoList(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item: str
    price: int
    is_done: bool | None = Field(default=None)
    # EX: {"id": 1, "item": "Buy groceries", "price": 20, "is_done": false}


class MessageToDoList(BaseModel):
    ## Typescript for GET
    message: List[TodoList]
    # EX: {message: [{item: 'egg', price: 30, id: 2, is_done: false},
    # {item: 'egg', price: 30, id: 2, is_done: false}]}


class MessageToDoItem(BaseModel):
    ## Typescript for POST, DELETE, PUT
    message: TodoList
    # EX: {message: {item: 'egg', price: 30, id: 2, is_done: false}}
