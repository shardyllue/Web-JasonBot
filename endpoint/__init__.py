from fastapi import APIRouter

from endpoint import (
    aouth, channel
)


routers = APIRouter()

routers.include_router(aouth.app)
routers.include_router(channel.app)