from pydantic import BaseModel

class UserAuth(BaseModel):

    username:str
    token:str
    device:str
