import uvicorn
from fastapi import FastAPI

from app.routers.v1.root import get_v1_root_router

app = FastAPI(
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
)


app.include_router(get_v1_root_router(), prefix="/api")

if __name__ == "__main__":
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=8080,
    )
    server = uvicorn.Server(config)
    server.run()
