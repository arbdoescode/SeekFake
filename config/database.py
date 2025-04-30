import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
from config import environment

firebase_config = {
    "apiKey": environment.apiKey,
    "authDomain": environment.authDomain,
    "databaseURL": environment.databaseURL,
    "projectId": environment.projectId,
    "storageBucket": environment.storageBucket,
    "messagingSenderId": environment.messagingSenderId,
    "appId": environment.appId,
    "measurementId": environment.measurementId,
}

# key_path = os.path.join(os.path.dirname(__file__), os.getenv("FOLDER_SECRET"), os.getenv("SERVICE_ACCOUNT"))

# if not firebase_admin._apps:
#     cred = credentials.Certificate(key_path)
#     firebase_app = firebase_admin.initialize_app(cred)

# db = firestore.client()

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()