from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)


engine = create_async_engine(
    url="postgresql+asyncpg://postgres:shardy@tgtesterbot.ru:5432/postgres"
)

Session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=True
)