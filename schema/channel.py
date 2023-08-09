from pydantic import BaseModel



class ChannelTable(BaseModel):


    user_id : int
    channel_id : int