from config.database import db
from module.Request.UserAuthReq import UserAuth
from module.Request.Account.RegisterUserReq import RegUserReq
from module.Response.BaseRes import BaseResp
# from module.ModelDB.UserTest import UsrTest
from config.database import firebase_config
from config.databaseAzure import conn
from service import fetchapikeys
# from config.databaseAzure import get_db
from datetime import datetime
import asyncio



# User Login & Registration

async def registerNewUser(item:RegUserReq):
    try:
        item.fullname = item.firstname.upper() + ' ' + item.lastname.upper()
        item.password = fetchapikeys.PasswordHash(item.password)
        item.recordcreateddate = datetime.now()
        
        def check_existing(username: str):
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM [User] WHERE Username = ?", (username,))
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            cursor.close()
            
            return [dict(zip(columns, row)) for row in rows]

       
        def run_query():
           
            existing_user = check_existing(item.username)

            if existing_user:  
                resp = BaseResp(Result=False, ResultMessage="User already exists")
                return resp
            else:
                try:
                   
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO [User] (Username, Fullname, Password, UserPlan, Active, RecCreatedDate) "
                        "VALUES (?, ?, ?, ?, ?, ?)",
                        (item.username, item.fullname, item.password, 'Free', True, item.recordcreateddate)
                    )
                   
                    conn.commit()
                    cursor.close()

                    
                    resp = BaseResp(Result=True, ResultMessage="User registered successfully")
                    return resp
                except Exception as e:
                   
                    resp = BaseResp(Result=False, ResultMessage=f"Error registering user: {e}")
                    return resp
        
        return await asyncio.to_thread(run_query)
    except Exception as e:
        resp = BaseResp(Result=False, ResultMessage=f"Error registering user: {e}")
        return resp



# Testing Phase

async def UserAuth(item: UserAuth):
    users = await asyncio.to_thread(db.child("ApiClients").get)

    if users.each() is None:
        return {"Error": "No user found in database"}

    for user in users.each():
        user_data = user.val()
        if user_data.get("Username") == item.username and user_data.get("Token") == item.token:
            return {"message": "User Found"}

    return {"message": "User Not Found"}

async def fetch_users_Test():
    try:
        def run_query():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM [UserTest]")
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            cursor.close()
            # conn.close()
            return [dict(zip(columns, row)) for row in rows]

        return await asyncio.to_thread(run_query)

    except Exception as e:
        return {"message": f"Error fetching users: {e}"}
    
async def registerNewUser_Test(item:UserAuth):
    try:
        def run_query():
            cursor = conn.cursor()
            cursor.execute("INSERT INTO [UserTest] (Username, Token) VALUES (?, ?)", (item.username, item.token))
            conn.commit()
            cursor.close()
            return {"message": "User registered successfully"}
        
        return await asyncio.to_thread(run_query)
    except Exception as e:
        return {"message": f"Error registering user: {e}"}
    
    




# async def register_user(user:UserAuth):
#      try:
#         def run_query():
#             dba = get_db()
#             dba = next(dba) 
#             new_user = UsrTest(Username=user.username, Token=user.token, Device=user.device)
#             dba.add(new_user)
#             dba.commit()
#             dba.refresh(new_user)
#             return new_user
        
#         return await asyncio.to_thread(run_query)
    
#      except Exception as e:
#         return {"message": f"Error registering user: {e}"}

#Finish Testing Phase






   