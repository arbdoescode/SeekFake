from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional


class RegUserReq(BaseModel):
    username: str
    fullname: Optional[str] = None
    firstname: str
    lastname: str
    password: str
    userplan: Optional[str] = None
    active: Optional[bool] = None
    recordcreateddate: Optional[date] = None
    
    @field_validator('username')
    def validate_username(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Username cannot be empty or blank")
        return v
    
    @field_validator('firstname')
    def validate_firstname(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Firstname cannot be empty or blank")
        return v
    
    @field_validator('lastname')
    def validate_lastname(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Lastname cannot be empty or blank")
        return v
    
    @field_validator('password')
    def validate_password(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Password cannot be empty or blank")
        return v
    