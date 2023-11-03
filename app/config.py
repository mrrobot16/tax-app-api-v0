from pydantic_settings import BaseSettings


# IMPORTANT NOTE: It is VERY IMPORTANT that these env variables are defined in .env and in heroku. 
# Else application will crash.
class ENV_VARIABLES(BaseSettings):
    APP_ENV: str
    APP_ENABLED: str
    OPENAI_ORG_ID: str
    OPENAI_API_KEY: str
    OPENAI_API_KEY_DEV: str
    OPENAI_API_KEY_PROD: str
    FIREBASE_ACCOUNT_TYPE: str
    FIREBASE_PROJECT_ID: str
    FIREBASE_PRIVATE_KEY: str
    FIREBASE_PRIVATE_KEY_DEV: str
    FIREBASE_PRIVATE_KEY_PROD: str
    FIREBASE_CLIENT_EMAIL: str
    FIREBASE_TOKEN_URI: str

    class Config:
        extra = "ignore"
        env_file = ".env"

env_variables = ENV_VARIABLES()
