import asyncio 
import hashlib

def Md5Format():
    result=hashlib.md5(b'BrokenRoad')
    print(result.hexdigest())

