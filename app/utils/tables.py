from typing import List
from app.schemas.tables import TableCreate, Table
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dao.tables import TableDAO


async def create_table(table: TableCreate, db: AsyncSession) -> Table:
    r = await TableDAO.add(session=db, **table.dict())
    return r


async def get_all_tables(db: AsyncSession) -> List[Table]:
    r = await TableDAO.get_all(session=db)
    return r


async def delete_table(table_id: int, db: AsyncSession) -> bool:
    r = await TableDAO.delete_base(session=db, id=table_id)
    return r
