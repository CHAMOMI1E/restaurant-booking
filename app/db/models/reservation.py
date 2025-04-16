from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime
from .base import Base


class Reservation(Base):
    __tablename__ = "reservation"

    custmer_name: Mapped[str] = mapped_column(nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey("table.id"), nullable=False)
    reservation_time: Mapped[datetime] = mapped_column(nullable=False)
    duration_minutes: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Reservation {self.id} for {self.customer_name}>"
