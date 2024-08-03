import os
from dotenv import load_dotenv
from .database import DBConn
from sqlmodel import create_engine


if os.getenv("USE_DOTENV", "False") == "True":
    load_dotenv(".env")

DBConn.load_envs()

## engine: an object that handles the communication with the database
engine = create_engine(DBConn.build_address())
