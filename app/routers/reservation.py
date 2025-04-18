from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.reservation import (
    get_reservation,
    create_reservation,
    delete_reservation,
)
from ..schemas.reservation import Reservation, ReservationCreate
from ..core.database import db_session
from ..content.reservations import (
    get_reservations_docs,
    delete_reservation_docs,
    add_reservation_docs,
)


router = APIRouter(prefix="/reservations")


@router.get("/", responses=get_reservations_docs, response_model=List[Reservation])
async def read_reservations_endpoint(db: AsyncSession = Depends(db_session)):
    result = await get_reservation(db=db)
    return result


@router.post("/", responses=add_reservation_docs, response_model=Reservation)
async def create_reservation_endpoint(
    reservation: ReservationCreate, db: AsyncSession = Depends(db_session)
):
    result = await create_reservation(db=db, reservation=reservation)
    return result


@router.delete(
    "/{reservation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses=delete_reservation_docs,
)
async def delete_reservation_endpoint(
    reservation_id: int, db: AsyncSession = Depends(db_session)
):
    await delete_reservation(reservation_id=reservation_id, db=db)
