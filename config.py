from pydantic_settings import BaseSettings, SettingsConfigDict

class ENV_VARIABLES_Settings(BaseSettings):
    APP_ENV: str
    APP_ENABLED: str
    DEBUG: str
    OPENAI_API_KEY: str
    OPENAI_API_KEY_DEV: str
    OPENAI_API_KEY_PROD: str
    OPENAI_ORG_ID: str
    FIREBASE_ACCOUNT_TYPE: str
    FIREBASE_PROJECT_ID: str
    FIREBASE_PRIVATE_KEY_ID: str
    FIREBASE_PRIVATE_KEY: str
    FIREBASE_PRIVATE_KEY_DEV: str
    FIREBASE_PRIVATE_KEY_PROD: str
    FIREBASE_CLIENT_EMAIL: str
    FIREBASE_CLIENT_ID: str
    FIREBASE_AUTH_URI: str
    FIREBASE_TOKEN_URI: str
    FIREBASE_AUTH_PROVIDER_X509_CERT_URL: str
    FIREBASE_CLIENT_X509_CERT_URL: str
    FIREBASE_UNIVERSE_DOMAIN: str

    model_config = SettingsConfigDict(env_file=".env")

config = ENV_VARIABLES_Settings()
