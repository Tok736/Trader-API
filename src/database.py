from typing import AsyncGenerator
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker, mapped_column, Mapped

from config import settings

Base: DeclarativeMeta = declarative_base()

engine = create_async_engine(settings.sqlalchemy_url)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class CreatedAt:
    created_at:   Mapped[datetime] = mapped_column(default=datetime.now)

class UpdatedAt:
    updated_at:   Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    ''' Function to get async database session '''
    async with async_session_maker() as session:
        yield session


