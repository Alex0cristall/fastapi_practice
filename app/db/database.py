from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings




# metadata_obj = MetaData()


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)
sync_session_fabric = sessionmaker(sync_engine)



async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)
async_session_fabric = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass



def crete_table_todolist():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
