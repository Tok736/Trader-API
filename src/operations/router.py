from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from .models import Operation
from .schemas import OperationSchemaRead, OperationSchemaCreate

router = APIRouter(
    prefix="/operations",
    tags=["operations"]
)

@router.get("/")
async def get_operations(
    session: AsyncSession = Depends(get_async_session)
) -> list[OperationSchemaRead]:
    statement = select(Operation)
    result = await session.scalars(statement)
    return result

@router.post("/")
async def add_operation(
    operation: OperationSchemaCreate,
    session: AsyncSession = Depends(get_async_session)
):
    statement = insert(Operation).values(operation.model_dump())
    result = await session.execute(statement)
    await session.commit()

    return {"status": "success", "operation_id": result.inserted_primary_key[0]}

