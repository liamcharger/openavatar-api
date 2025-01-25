from fastapi import FastAPI
from app.api.v1.endpoints import users

app = FastAPI()

@app.get("/")
def get_status():
    return {"status": "ok"}

app.include_router(users.router, prefix="/users", tags=["users"])