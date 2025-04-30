import asyncio
from fastapi import FastAPI
from middleware import token_auth
from config.database import db
from module.Request import UserAuthReq,ExampleReq
from service import auth,aigenerating
from starlette.requests import Request


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
    return auth.UserAuth(item)


@app.post("/aitest/")
async def aitest_call(msg:ExampleReq.SimpleReq):
    return {"message": aigenerating.aibasicresponse(msg)}

@app.get("/get-ip")
async def get_ip(request: Request):
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.client.host
    return {"ip": ip}
