from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from .models import Operation

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

# @router.get("/")
# async def get_all_operations(
#     session: AsyncSession = Depends(get_async_session)
# ) -> list[Operation]:
#     operations = await session.query(Operation).all()
#     return operations
