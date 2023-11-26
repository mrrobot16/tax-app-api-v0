from fastapi import FastAPI, status

from metadata import metadata
from routes import configure_routes
from middleware import configure_middleware

from config import APP_ENABLED, APP_ENV
from utils.sentry import configure_sentry

app = FastAPI(
    title = metadata["title"],
    description = metadata["description"],
    summary = metadata["summary"],
    version = metadata["version"],
    terms_of_service = metadata["terms_of_service"],
    contact = metadata["contact"],
    license_info = metadata["license_info"],
    openapi_tags = metadata["tags"],
    openapi_url = metadata["openapi_url"],
    docs_url="/docs",
    redoc_url="/documentation"
)

@app.get("/", tags = ["Health"])
async def health():
    return {
        "status": status.HTTP_200_OK, 
        "version": "0.0.1", 
        "APP_ENABLED": APP_ENABLED, 
        "APP_ENV": APP_ENV,
        "BEFORE_LAST_GIT_COMMIT_": "09de708bed4c9325389bdfa061adc480cab97c94"
    }

configure_sentry(app)
configure_middleware(app)
configure_routes(app)

