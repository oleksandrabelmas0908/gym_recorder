from os import getenv
from pydantic_settings import BaseSettings


# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# HOST = "127.0.0.1"
# PORT = "8000"


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///gym_recorder.db"
    db_echo: bool = True


settings = Settings()
