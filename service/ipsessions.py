from config.database import db
from module.Request.UserAuthReq import UserAuth
from config.database import firebase_config
import asyncio

async def getSessions(sess: str):
    sessions_data = await asyncio.to_thread(
        lambda: db.child("ApiClients").child("Sessions").child(sess).get().val()
    )

    tokens = []
    if not sessions_data:
        return {"response": "User not available"}
    
    # MainSession token
    main_session = sessions_data.get("MainSession", {})
    main_token = main_session.get("tokenUser")
    if main_token:
        tokens.append(main_token)

    # OtherSessions tokens
    other_sessions = sessions_data.get("OtherSessions", [])
    for session in other_sessions:
        if session and isinstance(session, dict):
            token = session.get("tokenUser")
            if token:
                tokens.append(token)

    return {"response": tokens}