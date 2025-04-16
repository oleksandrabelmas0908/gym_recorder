from fastapi import APIRouter


auth_router = APIRouter()


@auth_router.get("/")
def read_item(username: str | None = None):
    return {"User": username}