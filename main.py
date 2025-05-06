import asyncio
from fastapi import FastAPI
from middleware import token_auth
from config.database import db
from config.databaseAzure import conn
from module.Request import UserAuthReq,ExampleReq
from module.Response import UserRes
from service import auth,aigenerating,ipsessions
from starlette.requests import Request
from typing import List

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
async def UserAuthentication(item:UserAuthReq.UserAuth):
    response_text = await auth.UserAuth(item)
    return response_text


@app.post("/aitest/")
async def aitest_call(msg:ExampleReq.SimpleReq):
    response_text = await aigenerating.aibasicresponse(msg)
    return {"message": response_text}

@app.get("/get-ip")
async def get_ip(request: Request):
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.client.host
    return {"ip": ip}

@app.post("/ip-list/")
async def iplist_call(sess:ExampleReq.SimpleReq):
    response_text = await ipsessions.getSessions(sess.msg)
    return response_text

# Lindita Suta controllers

@app.get("/getusers/")
async def test_get_users():
    users = await auth.fetch_users()
    return users

  


# endregion LS
