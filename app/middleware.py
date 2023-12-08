import time
from datetime import datetime
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
        'http://app.taxapp.chat',
        'https://demo.taxapp.chat',
        'http://demo.taxapp.chat',
        'https://dev.taxapp.chat',
        'http://dev.taxapp.chat'
    ]
elif env_variables.APP_ENV == 'development':
    allowed_origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
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
        start_time = time.time()
        start_current_utc_time = datetime.utcnow()
        request_formatted_utc_time = start_current_utc_time.strftime("%Y-%m-%d %H:%M:%S")     
        
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        end_current_utc_time = datetime.utcnow()

        response_formatted_utc_time = end_current_utc_time.strftime("%Y-%m-%d %H:%M:%S")
        request_message = f" Request UTC timestamp: {request_formatted_utc_time}\n Request Method: {request.method}\n Request URL: {request.url.path}"
        response_message = f"Response UTC timestamp: {response_formatted_utc_time}\n Response status code: {response.status_code} X_Process_Time: {response.headers['X-Process-Time']}"
        message = f"{request_message}\n {response_message}"
        print('\n')
        print(message)

        return response