from typing import Annotated

from aiohttp import ClientSession
from fastapi import status, HTTPException, Depends
from jose import jwt, JWTError
from sqlalchemy import select, delete


from db import Session
from db.base import UserTable

from utils import config
from schema.oauth import (
    Telegram, 
    OauthHashData,
    AuthRequest,
    AuthResponse,
    AuthLogin,
    Auth
)



async def oauth_valid_bot(token : str) -> Telegram:
    """
    
    
    """
    
    async with ClientSession() as session:

        async with session.get(
            url=config.TELEGRAM_GETME.format(
                token=token
            )
        ) as response:
            _data = await response.json()

    return Telegram(**_data)


def oauth_hash_data(data : AuthRequest) -> OauthHashData:
    """
    
    
    
    """
    payload = data.model_dump()
    
    hashed = jwt.encode(payload, config.SECRET, algorithm=config.ALGORITHM)

    return OauthHashData(
        user_id=data.user_id,
        token=hashed
    )


async def auth_db_create_token(hashed_data : OauthHashData):
    """
    
    
    """

    db = Session()

    respose = await db.execute(select(UserTable).where(
        UserTable.hash_token == hashed_data.token
    ))

    if not respose.fetchone():

        db.add(UserTable(
            user_id=hashed_data.user_id,
            hashed_token=hashed_data.token
        )) 

        return await db.commit()


    await db.close()


async def oauth_register_webhook(token : str):
    """
    
    
    """

    async with ClientSession() as session:

        async with session.get(

            url=config.WEBHOOK.format(
                host=config.BOT_API,
                token=token,
            )

        ) as response:
            _status = response.status

    if _status != 200:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error webhook"
        )
    

async def oauth_register(data : AuthRequest) -> AuthResponse:
    """
    
    
    """

    bot = await oauth_valid_bot(data.token)

    if bot.ok is False:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=bot.description
        )

    hashed_data = oauth_hash_data(data)


    await auth_db_create_token(
        hashed_data=hashed_data
    )
    
    await oauth_register_webhook(
        token=data.token,
    )
    
    return AuthResponse(
        token=hashed_data,
        result=bot.result
    )
    

async def oauth_login(data : Annotated[AuthLogin, Depends()]):
    

    try:
        payload = jwt.decode(data.token, config.SECRET, algorithms=config.ALGORITHM)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="UNAUTHORIZED"
        )
    
    return Auth(
        token=payload.get("token"),
        user_id=payload.get("user_id"),
    )
    

async def oauth_delete(token : Auth):

    db = Session()

    await db.execute(delete(UserTable).where(
        UserTable.hash_token == token.token
    ))

    await db.close()
