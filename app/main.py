import uvicorn
from fastapi import FastAPI

from app.routers.v1.etc import get_etc_v1_router

app = FastAPI()


app.include_router(get_etc_v1_router())

if __name__ == "__main__":
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=8080,
    )
    server = uvicorn.Server(config)
    server.run()
