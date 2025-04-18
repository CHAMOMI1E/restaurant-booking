from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..content.tables import delete_table_docs, add_table_docs, get_table_docs
from ..schemas.tables import TableCreate, Table
from ..core.database import db_session
from ..services.tables import create_table, get_all_tables, delete_table


router = APIRouter(prefix="/table")


@router.post("/", responses=add_table_docs, response_model=Table)
async def add_table_endpoint(
    table: TableCreate, db: AsyncSession = Depends(db_session)
):
    result = await create_table(table=table, db=db)
    return result


@router.get("/", status_code=200, responses=get_table_docs, response_model=List[Table])
async def get_table_endpoint(db: AsyncSession = Depends(db_session)):
    result = await get_all_tables(db=db)
    return result


@router.delete(
    "/{table_id}", status_code=status.HTTP_204_NO_CONTENT, responses=delete_table_docs
)
async def delete_table_endpoint(table_id: int, db: AsyncSession = Depends(db_session)):
    await delete_table(table_id=table_id, db=db)
