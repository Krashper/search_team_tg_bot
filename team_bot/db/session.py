from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from contextlib import asynccontextmanager

async_engine = create_async_engine(url=DB_URL, echo=False)
async_session = async_sessionmaker(bind=async_engine)


@asynccontextmanager
async def async_session():
    