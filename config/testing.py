from datetime import datetime
import hashlib
import pyodbc
import os
from pydantic import BaseModel

class BaseResp(BaseModel):
    Result:bool
    ResultMessage:str

azureservername=os.getenv("AZURE_SQL_SERVER")
azuredatabase=os.getenv("AZURE_SQL_DATABASE")
azureusername=os.getenv("AZURE_USERNAME")
azurepassword=os.getenv("AZURE_PASSWORD")


conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={azureservername};"
    f"DATABASE={azuredatabase};"
    f"UID={azureusername};"
    f"PWD={azurepassword};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)



    
        

