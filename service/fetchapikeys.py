import asyncio 
import hashlib

#create method that, returns a random hashed id of (md5) format
def Md5Format():
    result=hashlib.md5(b'BrokenRoad')
    print(result.hexdigest())

Md5Format()
