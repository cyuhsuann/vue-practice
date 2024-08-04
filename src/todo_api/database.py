import os, typing
from sqlmodel import Field, SQLModel


## TODO:
class TodoList(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item: str
    price: int
    is_done: bool | None = Field(default=None)


class DBConn:
    username: typing.Optional[str] = None
    password: typing.Optional[str] = None
    db_name: typing.Optional[str] = None
    db_host: typing.Optional[str] = None
    db_port: typing.Optional[int] = None

    is_initialised = False

    @classmethod
    def build_address(cls):
        if not cls.is_initialised:
            raise ValueError(
                "DBConn class needs to load envs before it can generate addresses"
            )
        userpass = f"{cls.username}:{cls.password}"
        db_addr = f"{cls.db_host}:{cls.db_port}"
        return f"postgresql+psycopg2://{userpass}@{db_addr}/{cls.db_name}"

    @classmethod
    def load_envs(cls):
        var_env_pairs = [
            ("username", "DB_USER"),
            ("password", "DB_PASSWORD"),
            ("db_name", "DB_DATABASE"),
            ("db_host", "DB_HOST"),
            ("db_port", "DB_PORT"),
        ]

        errors = []
        for var, env in var_env_pairs:
            # set attribute
            setattr(cls, var, os.getenv(env))
            # get attribute
            if getattr(cls, var) is None:
                errors.append(env)

        if len(errors) > 0:
            msg = "\n  ".join(errors)
            raise ValueError(f"DB connection env vars missing:\n{msg}")

        cls.is_initialised = True


def setup_database():
    # Set up the database URL
    DBConn.load_envs()
    # Build the database URL
    return DBConn.build_address()
