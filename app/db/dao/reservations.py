from .base import BaseDAO
from .tables import TableDAO
from app.db.models.reservation import Reservation
from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy import and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession


class ReservationDAO(BaseDAO):
    model = Reservation

    @classmethod
    async def check_availability(
        cls, session: AsyncSession, table_id: int, start_time: datetime, duration: int
    ):
        table = await TableDAO.get_one_or_none(session=session, id=table_id)
        if table:
            start_time = start_time.replace(tzinfo=None)
            end_time = (start_time + timedelta(minutes=duration)).replace(tzinfo=None)

            print(start_time, end_time)
            query = select(cls.model).where(
                cls.model.table_id == table_id,
                cls.model.reservation_time < end_time,
                (
                    cls.model.reservation_time
                    + cls.model.duration_minutes * timedelta(minutes=1)
                )
                > start_time,
            )
            result = await session.execute(query)
            return result.scalars().first() is None
        else:
            raise HTTPException(status_code=400, detail="Столик не найден")
