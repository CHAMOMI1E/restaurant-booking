from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..content.tables import delete_store_docs
from ..schemas.tables import TableCreate, Table
from ..core.database import db_session
from ..utils.tables import create_table, get_all_tables, delete_table


router = APIRouter(prefix="/table")


@router.post("/", response_model=Table)
async def add_table(table: TableCreate, db: Session = Depends(db_session)):
    result = await create_table(table=table, db=db)
    return result


@router.get("/", response_model=List[Table])
async def get_table(db: Session = Depends(db_session)):
    result = await get_all_tables(db=db)
    return result


@router.delete("/{table_id}", responses=delete_store_docs)
async def delete_store(table_id: int, db: Session = Depends(db_session)):
    await delete_table(table_id=table_id, db=db)
