from .base import BaseDAO
from app.db.models.reservation import Reservation
from datetime import datetime, timedelta
from sqlalchemy import and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession


class ReservationDAO(BaseDAO):
    model = Reservation

    @classmethod
    async def check_availability(
        cls, session: AsyncSession, table_id: int, start_time: datetime, duration: int
    ):
        end_time = start_time + timedelta(minutes=duration)
        query = select(cls.model).where(
            and_(
                cls.model.table_id == table_id,
                or_(
                    cls.model.reservation_time.between(start_time, end_time),
                    (
                        cls.model.reservation_time
                        + cls.model.duration_minutes * timedelta(minutes=1)
                    )
                    > start_time,
                ),
            )
        )
        result = await session.execute(query)
        return result.scalars().first() is None
