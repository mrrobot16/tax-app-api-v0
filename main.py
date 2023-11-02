import uvicorn

from config import env_variables

if __name__ == "__main__":

    uvicorn.run(
        app="app.server:app",
        reload=True if env_variables.APP_ENV != "production" else False,
        workers=1,
    )