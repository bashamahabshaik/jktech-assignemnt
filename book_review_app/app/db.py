from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import async_scoped_session
import asyncio
# db = SQLAlchemy()
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI, future=True, echo=False, poolclass=NullPool)
async_session = async_sessionmaker(engine,expire_on_commit=False)
