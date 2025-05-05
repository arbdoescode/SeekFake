from config.database import db
from module.Request.UserAuthReq import UserAuth
from module.Response.SessionRes import SessionResponse
from config.database import firebase_config

import asyncio

async def getSessions(sess: str):
    # Fetch session data in a background thread
    sessions_data = await asyncio.to_thread(
        lambda: db.child("ApiClients").child("Sessions").child(sess).get().val()
    )

    if not sessions_data:
        return SessionResponse(success=False, message="User not available").to_json()

    # Return full session record (MainSession + OtherSessions)
    return SessionResponse(success=True, data=sessions_data).to_json()
