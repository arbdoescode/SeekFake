from pydantic import BaseModel
from typing  import Optional

class UsrResponse(BaseModel):
    id: int
    username:str
    token:str
    device:Optional[str]
