import os
from sqlmodel import Field, Session, SQLModel, create_engine
from dotenv import load_dotenv


load_dotenv()


class TodoList(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # (default=None, alias="id")
    item: str
    price: int | None = None


### Connecting postgresql with sqlalchemy

sqlite_file_name = "database.db"
# sqlite_url = f"sqlite://{sqlite_file_name}"  不適用
username = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_DATABASE"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]
db_address = (
    f"postgresql+psycopg2://{username}:{password}@{db_host}:{db_port}/{db_name}"
)


engine = create_engine(
    db_address,
    echo=True,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_todo():
    todo_1 = TodoList(item="pesto", price=10)
    todo_2 = TodoList(item="spaghetti", price=15)
    todo_3 = TodoList(item="broccoli", price=7)

    with Session(engine) as session:
        session.add(todo_1)
        session.add(todo_2)
        session.add(todo_3)

        session.commit()


# if __name__ == "__main__":
#     create_db_and_tables()


def main():
    create_db_and_tables()
    create_todo()


if __name__ == "__main__":
    main()
