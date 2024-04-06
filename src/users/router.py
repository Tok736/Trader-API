from typing import AsyncGenerator

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from exceptions import UserNotFound
from paginator import Paginator

from .models import User
from .schemas import UserRead


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_users(
    paginator: Paginator = Depends(),
    session: AsyncGenerator[AsyncSession, None] = Depends(get_async_session)
) -> list[UserRead]:
    ''' Endpoint to get all users from database with pagination '''
    statement = paginator(select(User))
    result = await session.scalars(statement)
    return result

@router.get("/{user_id}")
async def get_user(
    user_id: int,
    session: AsyncGenerator[AsyncSession, None] = Depends(get_async_session),
) -> UserRead:
    ''' Endpoint to get user by id '''
    statement = select(User).where(User.id == user_id)
    result = await session.scalars(statement)

    user = result.first()
    if user is None:
        raise UserNotFound

    return user