import firebase_admin
from firebase_admin import credentials, firestore
from app.config import env_variables

#  NOTE: Some variables are not needed for firestore.
FIREBASE_CREDENTIALS = {
    'type': env_variables.FIREBASE_ACCOUNT_TYPE,
    'project_id': env_variables.FIREBASE_PROJECT_ID,
    # 'private_key_id': config.FIREBASE_PRIVATE_KEY_ID,
    'private_key': env_variables.FIREBASE_PRIVATE_KEY,
    'client_email': env_variables.FIREBASE_CLIENT_EMAIL,
    # 'client_id': env_variables.FIREBASE_CLIENT_ID,
    # 'auth_uri': env_variables.FIREBASE_AUTH_URI,
    'token_uri': env_variables.FIREBASE_TOKEN_URI,
    # 'auth_provider_x509_cert_url': env_variables.FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
    # 'client_x509_cert_url': env_variables.FIREBASE_CLIENT_X509_CERT_URL,
    # 'universe_domain': env_variables.FIREBASE_UNIVERSE_DOMAIN
}

# NOTE: Initialize Firebase Admin SDK
credentials = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(credentials)

client = firestore.client()

# NOTE: Firestore database instance
firestore_db  = client
