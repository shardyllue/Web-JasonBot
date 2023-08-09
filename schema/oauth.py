from pydantic import BaseModel


class Result(BaseModel):

    id : int
    is_bot : bool
    first_name : str
    username : str
    can_join_groups : bool
    can_read_all_group_messages : bool
    supports_inline_queries : bool


class Telegram(BaseModel):

    ok : bool
    result : Result = None
    description : str = None


class OauthHashData(BaseModel):

    user_id : int
    token : str
    


class AuthRequest(BaseModel):


    user_id : int
    token : str


class AuthResponse(BaseModel):


    token : OauthHashData
    result : Result
    

class AuthLogin(BaseModel):

    token : str


class Auth(BaseModel):

    token : str
    user_id : int
