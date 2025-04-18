from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dao.reservations import ReservationDAO
from app.db.models import Reservation
from fastapi import HTTPException
from ..schemas.reservation import ReservationCreate


async def get_reservation(db: AsyncSession) -> List[Reservation]:
    return await ReservationDAO.get_all(session=db)


async def create_reservation(
    db: AsyncSession, reservation: ReservationCreate
) -> Reservation:
    is_available = await ReservationDAO.check_availability(
        session=db,
        table_id=reservation.table_id,
        start_time=reservation.reservation_time,
        duration=reservation.duration_minutes,
    )
    if is_available:
        return await ReservationDAO.add(session=db, **reservation.dict())
    else:
        raise HTTPException(status_code=400, detail="Выбранное время занято")


async def delete_reservation(db: AsyncSession, reservation_id: int):
    return await ReservationDAO.delete_base(session=db, id=reservation_id)
