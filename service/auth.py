from config.database import db
from module.Request.UserAuthReq import UserAuth
from config.database import firebase_config
from config.databaseAzure import conn
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

async def fetch_users():
    try:
        def run_query():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM [User]")
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            cursor.close()
            # conn.close()
            return [dict(zip(columns, row)) for row in rows]

        return await asyncio.to_thread(run_query)

    except Exception as e:
        return {"message": f"Error fetching users: {e}"}






   