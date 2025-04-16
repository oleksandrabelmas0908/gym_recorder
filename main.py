from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.models import Base, db_helper

from auth.view import auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run(app)
