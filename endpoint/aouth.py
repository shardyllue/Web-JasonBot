from typing import Annotated

from fastapi import APIRouter, status, Depends

from service.oauth import oauth_register
from service.oauth import oauth_login, oauth_delete

from schema.oauth import AuthRequest, AuthResponse



app = APIRouter(
    prefix="/oauth",
    tags=["Auth"]
)


@app.post(
    path="/register",
    description="Register user bot",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(data : AuthRequest):
    """
    
    Register user
    
    """
    return await oauth_register(data)



@app.post(
    path="/delete",
    description="Delete user account",
    status_code=status.HTTP_202_ACCEPTED,
)
async def register(token = Depends(oauth_login)):
    """
    
    Register user
    
    """
    await oauth_delete(token)

    return status.HTTP_202_ACCEPTED

