from config.database import db
from module.Request.UserAuthReq import UserAuth
from config.database import firebase_config
import asyncio

async def UserAuth(item: UserAuth):
    users = await asyncio.to_thread(db.child("ApiClients").get)

    if users.each() is None:
        return {"Error": "No user found in database"}

    for user in users.each():
        user_data = user.val()
        if user_data.get("Username") == item.username and user_data.get("Token") == item.token:
            return {"message": "User Found"}

    return {"message": "User Not Found"}





   