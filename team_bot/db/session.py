from team_bot.config import config

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from contextlib import asynccontextmanager

async_engine = create_async_engine(url=config.SQLALCHEMY_DB_URL.unicode_string(), echo=False)


@asynccontextmanager
async def async_session():
    async_session = async_sessionmaker(bind=async_engine)
    
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
        finally:
            await session.close()
    