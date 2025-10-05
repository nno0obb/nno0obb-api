from functools import lru_cache

from fastapi import APIRouter
from fastapi.responses import JSONResponse, PlainTextResponse

etc_v1_router = APIRouter(prefix="/api/v1", tags=["etc"])


@etc_v1_router.get("/ping")
def get_ping():
    return PlainTextResponse("pong")


@etc_v1_router.get("/info")
def get_info():
    return JSONResponse(
        {
            "app": {
                "name": "nno0obb-api",
            }
        }
    )


@lru_cache()
def get_etc_v1_router():
    return etc_v1_router
