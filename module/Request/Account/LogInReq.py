from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class LogInUsr(BaseModel):
    username:str
    password:str
    
    
@field_validator('username')
def validate_username(cls, v):
    if not v or v.strip() == "":
        raise ValueError("Username cannot be empty or blank")
    return v
    
@field_validator('password')
def validate_firstname(cls, v):
    if not v or v.strip() == "":
        raise ValueError("Password cannot be empty or blank")
    return v