from pydantic_settings import BaseSettings, SettingsConfigDict


# IMPORTANT NOTE: It is very important that these env variables are defined in .env and in heroku. 
# Else application will crash.

class ENV_VARIABLES_Settings(BaseSettings):
    APP_ENV: str
    APP_ENABLED: str
    # DEBUG: str = None
    # OPENAI_API_KEY: str = None
    OPENAI_API_KEY_DEV: str
    # OPENAI_API_KEY_PROD: str = None
    # OPENAI_ORG_ID: str = None
    FIREBASE_ACCOUNT_TYPE: str
    FIREBASE_PROJECT_ID: str
    # FIREBASE_PRIVATE_KEY_ID: str = None
    FIREBASE_PRIVATE_KEY: str
    FIREBASE_PRIVATE_KEY_DEV: str
    FIREBASE_PRIVATE_KEY_PROD: str
    FIREBASE_CLIENT_EMAIL: str
    # FIREBASE_CLIENT_ID: str = None
    # FIREBASE_AUTH_URI: str = None
    FIREBASE_TOKEN_URI: str
    # FIREBASE_AUTH_PROVIDER_X509_CERT_URL: str = None
    # FIREBASE_CLIENT_X509_CERT_URL: str = None
    # FIREBASE_UNIVERSE_DOMAIN: str = None

    model_config = SettingsConfigDict(env_file=".env")

env_variables = ENV_VARIABLES_Settings()
