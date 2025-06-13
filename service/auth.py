from config.database import db
from module.Request.UserAuthReq import UserAuth
from module.Request.Account.RegisterUserReq import RegUserReq
from module.Request.Account.LogInReq import LogInUsr
from module.Response.BaseRes import BaseResp
# from module.ModelDB.UserTest import UsrTest
from config.database import firebase_config
from config.databaseAzure import conn
from service import fetchapikeys
# from _Testing.databaseTest import SessionLocal
from datetime import datetime, timedelta
from config.logger_config import LoggingHelper
import asyncio


# User Login/LogOut & Registration

async def registerNewUser(item:RegUserReq):
    try:
        item.fullname = item.firstname.upper() + ' ' + item.lastname.upper()
        item.password = fetchapikeys.PasswordHash(item.password)
        item.recordcreateddate = datetime.now()
        
        def check_existing(username: str):
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM [User] WHERE Username = ?", (username))
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

async def logIn(usr:LogInUsr):
    try:
        hashedpassword = fetchapikeys.PasswordHash(usr.password)
        
        def check_existing(username: str,password:str):
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM [User] WHERE Username = ? and Password = ?", (usr.username,hashedpassword))
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            cursor.close()
            
            return [dict(zip(columns, row)) for row in rows]

       
        def run_query():
           
            existing_user = check_existing(usr.username,hashedpassword)

            
            if not existing_user:  
                resp = BaseResp(Result=False, ResultMessage="Incorrect username or password")
                return resp
            else:
                try:
                    token = fetchapikeys.usersessionid()
                    lastLog = datetime.now()
                    experationDate = datetime.now() + timedelta(days=3)
                    
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO [Session] (Token, Username, ExperationDate, LastLog, Device, DeviceID, IP)"
                        "VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (token, usr.username, experationDate, lastLog, 'Test', 'Test','Test')
                    )
                   
                    conn.commit()
                    cursor.close()

                    
                    resp = BaseResp(Result=True, ResultMessage="User logged in successfully",Detail=[{"token": token}])
                    return resp
                except Exception as e:
                   
                    resp = BaseResp(Result=False, ResultMessage=f"Error log in user: {e}")
                    return resp
        
        return await asyncio.to_thread(run_query)
    except Exception as e:
        resp = BaseResp(Result=False, ResultMessage=f"Error log in user: {e}")
        return resp
   
async def logout(token:str):
    try:
        def run_query():
            query = "DELETE FROM [Session] WHERE Token = ?"
            try:
                        
                cursor = conn.cursor()
                cursor.execute(query,(token))
                conn.commit()
                cursor.close()

                resp = BaseResp(Result=True, ResultMessage="User logged out successfully")
                return resp
            except Exception as e:
                    
                resp = BaseResp(Result=False, ResultMessage=f"Error log out user: {e}")
                return resp
            
        return await asyncio.to_thread(run_query)
    except Exception as e:
        resp = BaseResp(Result=False, ResultMessage=f"Error log out user: {e}")
        return resp
             
async def getUser(username: str):
    try:
        
        logger = LoggingHelper.get_logger("UserService")
        logger.info(f"Fetching user: {username}")
        
        def run_query():
              
            cursor = conn.cursor()
            cursor.execute("SELECT [Username],[Fullname],[UserPlan] FROM [User] WHERE Username = ?", (username,))
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            cursor.close()
            
            return [dict(zip(columns, row)) for row in rows]
            
        result = await asyncio.to_thread(run_query)
        
        logger = LoggingHelper.get_logger("UserService")
        LoggingHelper.log_structured(logger, result)
        
        return result
    except Exception as e:
        resp = BaseResp(Result=False, ResultMessage=f"Error geting user: {e}")
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
#              with SessionLocal() as db:
#                 new_user = UsrTest(Username=user.username, Token=user.token, Device=user.device)
#                 db.add(new_user)
#                 db.commit()
#                 db.refresh(new_user)
#                 resp = BaseResp(Result=True, ResultMessage="User registered successfully")
#                 return resp
            
#         return await asyncio.to_thread(run_query)
    
#      except Exception as e:
#         resp = BaseResp(Result=False, ResultMessage=f"Error registering user: {e}")
#         return resp

#Finish Testing Phase






   