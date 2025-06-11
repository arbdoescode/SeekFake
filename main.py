import asyncio
from fastapi import FastAPI,Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from middleware import token_auth
from config.database import db
# from config.databaseAzure import conn
from module.Request import UserAuthReq,ExampleReq
from module.Response import UserRes
from module.Request.Account import RegisterUserReq
from module.Request.Account import LogInReq
from module.Response.BaseRes import BaseResp
from service import auth,aigenerating,ipsessions
from starlette.requests import Request
from config.logger_config import get_logger
from typing import List

app = FastAPI()

app.add_middleware(token_auth.CheckValueMiddleware, skip_paths=["/test/","/register/","/login/"])



# Example methods

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
   
   
#LOGIN/LogOut & REGISTER   
 
@app.post("/register/")
async def RegisterNewUser(item:RegisterUserReq.RegUserReq):
    response_text = await auth.registerNewUser(item)
    return response_text  

@app.post("/login/")
async def RegisterNewUser(item:LogInReq.LogInUsr):
    response_text = await auth.logIn(item)
    return response_text  

# @app.get("/logout/{token}")
# async def RegisterNewUser(token: str):
#     response_text = await auth.logout(token)
#     return response_text  

@app.get("/logout/")
async def RegisterNewUser(request: Request):
    token = request.headers.get("token")
    response_text = await auth.logout(token)
    return response_text  

#TESTING

@app.get("/test__getuser/")
async def test__get_users(request: Request):
    username = request.state.username  
    users = await auth.getUser(username) 
    return users

@app.get("/test-getusers/")
async def test_get_users():
    users = await auth.fetch_users_Test()
    return users

@app.post("/test-register/")
async def RegisterNewUser(item:UserAuthReq.UserAuth):
    response_text = await auth.registerNewUser_Test(item)
    return response_text

@app.post("/testnew-register/")
async def RegisterNewUser(item:UserAuthReq.UserAuth):
    response_text = await auth.register_user(item)
    return response_text

#FINISH TESTING

# endregion LS
