from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from .dependencies import User 


async def get_user_db(
    session: AsyncSession = Depends(get_async_session)
) -> AsyncGenerator[AsyncGenerator, None]:
    yield SQLAlchemyUserDatabase(session, User)
    
