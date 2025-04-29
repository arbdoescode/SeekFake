from fastapi import FastAPI
from middleware import token_auth
from config.database import db
app = FastAPI()

app.add_middleware(token_auth.CheckValueMiddleware, skip_paths=["/test/"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/")
async def test_call():
    raport_ref = db.child("test")
    data = raport_ref.get().val()

    return {"message": "data"}