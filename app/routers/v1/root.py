from functools import lru_cache

from fastapi import APIRouter
from fastapi.responses import JSONResponse, PlainTextResponse

v1_root_router = APIRouter(prefix="/v1", tags=["root"])


@v1_root_router.get("/ping")
def get_ping():
    return PlainTextResponse("pong")


@v1_root_router.get("/info")
def get_info():
    return JSONResponse(
        {
            "app": {
                "name": "nno0obb-api",
            }
        }
    )


@lru_cache()
def get_v1_root_router():
    return v1_root_router
