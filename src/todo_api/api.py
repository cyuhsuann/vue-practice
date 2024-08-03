from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, TypeVar
from .database import TodoList
from .app import engine


class MessageToDoList(BaseModel):
    ## Typescript for GET
    message: List[TodoList]


class MessageToDoItem(BaseModel):
    ## Typescript for POST, DELETE, PUT
    message: TodoList


app = FastAPI()

## DEVNOTE: the backend need to have a list of 'allowed origins' to let the
# frondend send its request
origins = ["http://localhost:5173", "http://localhost:5175"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


## way way important to show in front of browser!
def get_session():
    with Session(engine) as session:
        yield session


@app.get("/todolist", response_model=MessageToDoList)
def read_todolists():
    # remember this is the simple way to connect the database, but still can
    # use Depends
    with Session(engine) as sess:
        todolists = sess.exec(select(TodoList)).all()
    return {"message": todolists}


# # defined in .database, or .todolist or something
def get_todolist_items():
    with Session(engine) as sess:
        todolists = sess.exec(select(TodoList)).all()
    return todolists


@app.post("/todolist", response_model=MessageToDoItem)
def create_todolist(todolist: TodoList) -> MessageToDoItem:
    with Session(engine) as session:
        session.add(todolist)
        session.commit()
        session.refresh(todolist)
    # print("********", todolist)
    # print("\n\n\n\n\n")
    return MessageToDoItem(message=todolist)


@app.delete("/todolist/{todo_id}", response_model=MessageToDoItem)
def delete_todoList(
    todo_id: int, session: Session = Depends(get_session)
) -> MessageToDoItem:
    todo_item = session.get(TodoList, todo_id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    session.delete(todo_item)
    session.commit()
    return MessageToDoItem(message=todo_item)


@app.put("/todolist/{todo_id}", response_model=MessageToDoItem)
def update_todoList(
    todo_id: int, todo_update: TodoList, session: Session = Depends(get_session)
) -> MessageToDoItem:
    todo_item = session.get(TodoList, todo_id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    todo_item.id = todo_update.id
    todo_item.item = todo_update.item
    todo_item.price = todo_update.price
    todo_item.is_done = todo_update.is_done

    session.add(todo_item)
    session.commit()
    session.refresh(todo_item)

    return MessageToDoItem(message=todo_item)
