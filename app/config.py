from pydantic_settings import BaseSettings, SettingsConfigDict


# IMPORTANT NOTE: It is very important that these env variables are defined in .env and in heroku. 
# Else application will crash.

class ENV_VARIABLES_Settings(BaseSettings):
    APP_ENV: str
    APP_ENABLED: str
    OPENAI_API_KEY: str
    OPENAI_API_KEY_DEV: str
    OPENAI_API_KEY_PROD: str
    OPENAI_ORG_ID: str
    FIREBASE_ACCOUNT_TYPE: str
    FIREBASE_PROJECT_ID: str
    FIREBASE_PRIVATE_KEY: str
    FIREBASE_PRIVATE_KEY_DEV: str
    FIREBASE_PRIVATE_KEY_PROD: str
    FIREBASE_CLIENT_EMAIL: str
    FIREBASE_TOKEN_URI: str

    model_config = SettingsConfigDict(env_file=".env")

env_variables = ENV_VARIABLES_Settings()
