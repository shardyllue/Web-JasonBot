from typing import Annotated

from fastapi import APIRouter, Depends, status

from schema.oauth import Auth
from service.oauth import oauth_login
from service.channel import register_channel

app = APIRouter(
    prefix="/channel",
    tags=["Channel"]
)



@app.post(
    path="/new"
)
async def add_new_channel(
    auth : Annotated[Auth, Depends(oauth_login)],
    channel_id : int
):
    await register_channel(
        user_id=auth.user_id,
        channel_id=channel_id
    )

    return status.HTTP_201_CREATED