from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.settings import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_db = async_sessionmaker(
            blind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
