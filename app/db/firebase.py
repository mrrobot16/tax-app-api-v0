import firebase_admin
from firebase_admin import credentials, firestore
from app.config import env_variables

# NOTE: The below variables are only needed for firestore, there will be other firebase services that will be needed 
FIREBASE_CREDENTIALS = {
    'type': env_variables.FIREBASE_ACCOUNT_TYPE,
    'project_id': env_variables.FIREBASE_PROJECT_ID,
    'private_key': env_variables.FIREBASE_PRIVATE_KEY,
    'client_email': env_variables.FIREBASE_CLIENT_EMAIL,
    'token_uri': env_variables.FIREBASE_TOKEN_URI,
}

# NOTE: Initialize Firebase Admin SDK
credentials = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(credentials)

# NOTE: Firestore database instance
client = firestore.client()
firestore_db  = client
