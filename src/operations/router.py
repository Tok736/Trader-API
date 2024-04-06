from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

from database import get_async_session
from paginator import Paginator

from .models import Operation
from .schemas import OperationSchemaRead, OperationSchemaCreate

router = APIRouter(
    prefix="/operations",
    tags=["operations"]
)

@router.get("/")
@cache(expire=60)
async def get_operations(
    paginator: Paginator = Depends(),
    session: AsyncSession = Depends(get_async_session)
) -> list[OperationSchemaRead]:
    ''' Function to get paginated operations '''
    statement = paginator(select(Operation))
    result = await session.scalars(statement)
    return result

@router.post("/")
async def add_operation(
    operation: OperationSchemaCreate,
    session: AsyncSession = Depends(get_async_session)
):
    ''' Function to insert new operation. Returns id of inserted operation '''
    statement = insert(Operation).values(operation.model_dump())
    result = await session.execute(statement)
    await session.commit()

    return {"operation_id": result.inserted_primary_key[0]}


from time import sleep
@router.get("/calc")
@cache(expire=60)
async def big_calculations(
    calc_time: int,
):
    ''' Long long calculations '''
    sleep(calc_time)
    
    return {"result": "calculations are completed"}