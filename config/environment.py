import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("FIREBASE_API_KEY")
authDomain = os.getenv("FIREBASE_AUTH_DOMAIN")
databaseURL = os.getenv("FIREBASE_DATABASE_URL")
projectId = os.getenv("FIREBASE_PROJECT_ID")
storageBucket = os.getenv("FIREBASE_STORAGE_BUCKET")
messagingSenderId = os.getenv("FIREBASE_MESSAGING_SENDER_ID")
appId = os.getenv("FIREBASE_APP_ID")
measurementId = os.getenv("FIREBASE_MEASURMENT_ID")

foldersecret = os.getenv("FOLDER_SECRET")
serviceacc = os.getenv("SERVICE_ACCOUNT")

exampleapikey = os.getenv("YOUR_AI_API_KEY")

