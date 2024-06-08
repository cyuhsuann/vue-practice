from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from .database import TodoList, engine, create_db_and_tables


class TodoListUpdate(BaseModel):  # for PUT function
    item: str
    price: int


app = FastAPI()


origins = [
    "http://localhost:5173",
    # "http://localhost",
    # "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def lifespan(app: FastAPI):
    create_db_and_tables()


def get_session():  # way way important to show in front of browser!
    with Session(engine) as session:
        yield session


@app.get("/todolist", response_model=List[TodoList])
def read_todolists(
    session: Session = Depends(get_session),
):  # then Depends can connect to the browser
    todolists = session.exec(select(TodoList)).all()
    return todolists


@app.post("/todolist")
def create_todolist(todolist: TodoList):
    with Session(engine) as session:
        session.add(todolist)
        session.commit()
        session.refresh(todolist)
    return {"message": "Accept Database"}


@app.delete("/todolist/{todo_id}")
def delete_todoList(todo_id: int, session: Session = Depends(get_session)):
    todo_item = session.get(TodoList, todo_id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    session.delete(todo_item)
    session.commit()
    return todo_item


@app.put("/todolist/{todo_id}")
def update_todoList(
    todo_id: int, todo_update: TodoListUpdate, session: Session = Depends(get_session)
):
    todo_item = session.get(TodoList, todo_id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    todo_item.item = todo_update.item
    todo_item.price = todo_update.price
    session.add(todo_item)
    session.commit()
    session.refresh(todo_item)
    return {"message": todo_item}
