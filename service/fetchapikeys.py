import asyncio 
import hashlib
import uuid

def Md5Format(sessionid:str):
    result=hashlib.md5(str)
    return result
    

def usersessionid():
    user_session_id = str(uuid.uuid4())
    return user_session_id
     
def PasswordHash(password:str):
    result = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return result
