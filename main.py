import uvicorn
from fastapi import FastAPI

from auth.view import auth_router

app = FastAPI()
app.include_router(auth_router)




if __name__ == '__main__':
    uvicorn.run(app)