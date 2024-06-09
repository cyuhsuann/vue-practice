# TODO: research why do I need this code for the first line
## uvicorn todo_api:app --reload  OR
## uvicorn todo_api.api:app --reload
from .api import app
