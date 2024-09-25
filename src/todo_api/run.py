import uvicorn
from todo_api.database import DBConn

print("import name:", __name__)


def main():
    DBConn.load_envs()
    uvicorn.run("todo_api.api:app", host="0.0.0.0", port=8080, reload=True)
    ## uvicorn: An ASGI web server, for Python


if __name__ == "__main__":
    main()
    ## provides a standard entry point to run scripts and standalone apps
    ## This can prevent certain code from being unintentionally executed when the
    # (unexpected) module is imported.
