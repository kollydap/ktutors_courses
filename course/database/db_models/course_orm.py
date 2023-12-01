from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases

from sqlalchemy import Column, Integer, String
import sqlalchemy


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
database = databases.Database(SQLALCHEMY_DATABASE_URL)


metadata = sqlalchemy.MetaData()

Course = sqlalchemy.Table(
    "course",
    metadata,
    Column("course_uid", Integer, primary_key=True),
    Column("tutor_uid", Integer, index=True),
    Column("title", String),
    Column("description", String),
    Column("duration", String),
    Column("price", String),
)


engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
