from db import Session
from db.base import ChannelTable

from sqlalchemy import select




async def register_channel(user_id : int, channel_id : int):
    
    db = Session()

    channel = await db.execute(select(ChannelTable).where(
        ChannelTable.channel_id == channel_id
    ))

    if not channel.fetchone():

        db.add(ChannelTable(
            user_id=user_id,
            channel_id=channel_id
        ))

        await db.commit()

    await db.close()

