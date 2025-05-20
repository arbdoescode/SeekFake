import pyodbc
import os
from config import environment


azureservername=environment.azureservername
azuredatabase=environment.azuredatabase
azureusername=environment.azureusername
azurepassword=environment.azurepassword


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

    
        

