from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints import users

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_status():
    return {"status": "ok"}

app.include_router(users.router, prefix="/users", tags=["users"])