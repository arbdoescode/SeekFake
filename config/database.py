import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

load_dotenv()

firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASURMENT_ID"),
}

# key_path = os.path.join(os.path.dirname(__file__), os.getenv("FOLDER_SECRET"), os.getenv("SERVICE_ACCOUNT"))

# if not firebase_admin._apps:
#     cred = credentials.Certificate(key_path)
#     firebase_app = firebase_admin.initialize_app(cred)

# db = firestore.client()

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()