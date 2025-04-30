from pydantic import BaseModel

class BaseReq(BaseModel):
    class Auth(BaseModel):
        tokernUser:str
        connsource:str

    class UserClient(BaseModel):
        usernameclient:str
        clientid:str
    ref: str
    device: str
    auth: Auth
    user: UserClient