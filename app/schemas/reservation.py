from pydantic import BaseModel, ConfigDict, Field, validator, field_validator
from datetime import datetime, timezone


class ReservationBase(BaseModel):
    customer_name: str
    table_id: int = Field(..., gt=0)
    reservation_time: datetime
    duration_minutes: int = Field(..., gt=0)


class ReservationCreate(ReservationBase):

    @validator("reservation_time", pre=True)
    def validate_reservation_time(cls, value):
        if isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value)
            except ValueError:
                raise ValueError(
                    "Неверный формат времени. Используйте ISO 8601 (например, 2025-04-17T12:00:00Z)"
                )
        elif isinstance(value, datetime):
            dt = value
        else:
            raise TypeError("reservation_time должен быть строкой или datetime")

        if dt.tzinfo is not None:
            dt = dt.replace(tzinfo=None)

        current_time = datetime.utcnow().replace(tzinfo=None)
        if dt < current_time:
            raise ValueError(
                "Невозможно добавить бронь на прошлое. Введите в reservation_time будущее время!"
            )

        return dt


class Reservation(ReservationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
