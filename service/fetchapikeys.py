import asyncio 
import hashlib
from config.database import db

def Md5Format():
    result=hashlib.md5(b'BrokenRoad')
    print(result.hexdigest())
