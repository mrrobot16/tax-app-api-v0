from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from routers import items
# from dependencies import get_query_token, get_token_header

app = FastAPI()

app.include_router(items.router)

@app.get("/")
async def root():
    # return JSONResponse(content={"status": 200}, status_code = status.HTTP_200_OK)
    return {"status": 200}