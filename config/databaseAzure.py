import pyodbc
import os
from config import environment
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


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

# DATABASE_URL = (
#     f"mssql+pyodbc://{azureusername}:{azurepassword}"
#     f"@{azureservername}/{azuredatabase}"
#     "?driver=ODBC+Driver+18+for+SQL+Server"
#     "&Encrypt=yes"
#     "&TrustServerCertificate=no"
#     "&Connection Timeout=30"
# )

# engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal() 
    
#     yield db  
    
        

