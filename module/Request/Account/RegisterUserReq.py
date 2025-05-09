from pydantic import BaseModel

class RegUserReq(BaseModel):
    username: str
    fullname: str
    password: str
    userplan: str
    active: bool