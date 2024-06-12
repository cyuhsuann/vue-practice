# TODO: research why do I need this code for the first line
##
## {{ uvicorn todo_api:app --reload }} Entry Point for the Application OR
## Application Configuration
##
## {{ uvicorn todo_api.api:app --reload }} tells Uvicorn to look for the `app`
## instance in the api.py file inside the todo_api package.
from .api import app
