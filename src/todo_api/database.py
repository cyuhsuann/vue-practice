import os, typing
from dotenv import load_dotenv

if os.getenv("USE_DOTENV", "False") == "True":
    load_dotenv(".env")
    ## echo $USE_DOTENV
    ## ## $USE_DOTENV=True
    ## TODO: does there have other methods to check True or False?


class DBConn:
    username: typing.Optional[str] = None
    password: typing.Optional[str] = None
    db_name: typing.Optional[str] = None
    db_host: typing.Optional[str] = None
    db_port: typing.Optional[int] = None

    is_initialised = False
    ## the necessary environment variables (like database username, password ...)
    # have not been loaded.

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
        ## After the environment variables are successfully loaded by the load_envs method,
        # it is set to True. The class now has all the info it needs to proceed, and it is
        # safe to generate the database connection string.


DBConn.load_envs()
