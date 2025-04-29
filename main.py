import asyncio
from fastapi import FastAPI
from middleware import token_auth
from config.database import db
from module.Request.UserAuthReq import UserAuth
from service import auth

app = FastAPI()

app.add_middleware(token_auth.CheckValueMiddleware, skip_paths=["/test/"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/")
async def test_call():
    raport_ref = db.child("test")
    data = raport_ref.get().val()

    return {"message": data}

@app.post("/user/")
async def UserAuthentication(item:UserAuth):
    return auth.UserAuth(item)
  

