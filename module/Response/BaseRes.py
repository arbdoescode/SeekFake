from pydantic import BaseModel
from typing import List, Optional

class BaseResp(BaseModel):
    Result:bool
    ResultMessage:str
    Detail: Optional[List[dict]] = None