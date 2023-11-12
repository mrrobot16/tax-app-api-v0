import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.config import env_variables

if env_variables.APP_ENV == 'production':
    allowed_origins = [
        'https://irs-copilot.vercel.app/', 
        'https://irs-copilot.vercel.app', 
        'https://www.taxapp.chat', 
        'http://www.taxapp.chat',
        'https://app.taxapp.chat',
        'http://app.taxapp.chat'
    ]
elif env_variables.APP_ENV == 'development':
    allowed_origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

def configure_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        print("APP_ENV: ", env_variables.APP_ENV)
        print("APP_ENABLED: ", env_variables.APP_ENABLED)
        request_message = f"Request Method: {request.method} Request URL: {request.url.path}"
        print(request_message)
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        response_message = f"Response status code: {response.status_code} X_Process_Time: {response.headers['X-Process-Time']}"
        print(response_message)
        return response