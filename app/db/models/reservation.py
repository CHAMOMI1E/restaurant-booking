from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from .base import Base


class Reservation(Base):
    __tablename__ = "reservation"

    customer_name: Mapped[str] = mapped_column(nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey("table.id"), nullable=False)
    reservation_time: Mapped[datetime] = mapped_column(nullable=False)
    duration_minutes: Mapped[int] = mapped_column(nullable=False)

    table: Mapped["Table"] = relationship(back_populates="reservations")  # type: ignore

    def __repr__(self):
        return f"<Reservation {self.id} for {self.customer_name}>"
