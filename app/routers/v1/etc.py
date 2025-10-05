from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

etc_v1_router = APIRouter(prefix="/api/v1", tags=["etc"])


@etc_v1_router.get("/ping")
def get_ping():
    return PlainTextResponse("pong")


def get_etc_v1_router():
    return etc_v1_router
