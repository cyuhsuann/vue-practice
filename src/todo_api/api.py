from fastapi import HTTPException, Depends
from sqlmodel import select, Session, create_engine
from .database import DBConn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .models import TodoList, MessageToDoItem, MessageToDoList


app = FastAPI()


## it is not necessary but it is useful for debugging and monitoring
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    ## log request info
    # EX: Request: GET http://localhost:8000/todolist
    # EX: Request: PUT http://localhost:8000/todolist/2
    print(f"Request: {request.method} {request.url}")

    ## pass the request to the next middleware or route handler
    response = await call_next(request)

    # log response info
    # EX: Response: 200
    print(f"Response: {response.status_code}")

    return response


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


## to provide or manage database sessions effectively, and avoid repetitive code
# in each route handler
def get_session():
    ## engine: an object that handles the communication with the database
    engine = create_engine(DBConn.build_address())
    with Session(engine) as session:
        yield session


## it is a specific API endpoint func used to retrieve todolist data from the database
@app.get("/todolist", response_model=MessageToDoList)
def read_todolists():
    # remember this is the simple way to connect the database, but still can
    # use Depends
    engine = create_engine(DBConn.build_address())
    with Session(engine) as sess:
        todolists = sess.exec(select(TodoList)).all()
    return {"message": todolists}


@app.post("/todolist", response_model=MessageToDoItem)
def create_todolist(todolist: TodoList) -> MessageToDoItem:
    engine = create_engine(DBConn.build_address())
    with Session(engine) as session:
        session.add(todolist)
        session.commit()
        session.refresh(todolist)
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
    session.commit()  ## Commits the changes, making them permanent in the database.
    session.refresh(todo_item)

    return MessageToDoItem(message=todo_item)
