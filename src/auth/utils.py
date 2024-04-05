from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import User 

from database import get_async_session

async def get_user_db(
        session: AsyncSession = Depends(get_async_session)
    ) -> AsyncGenerator[AsyncGenerator, None]:
    yield SQLAlchemyUserDatabase(session, User)
    
