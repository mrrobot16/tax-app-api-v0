from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from utils import use_route_names_as_operation_ids
from routers import items

app = FastAPI()

app.include_router(items.router)

@app.get("/")
async def root():
    return JSONResponse(content={"status": 200}, status_code = status.HTTP_200_OK)

use_route_names_as_operation_ids(app)