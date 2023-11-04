from fastapi import FastAPI, status

from app.metadata import metadata

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

@app.get("/")
async def health():
    return {"status": status.HTTP_200_OK }


