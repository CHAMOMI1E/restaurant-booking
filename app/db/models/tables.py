from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Table(Base):
    __tablename__ = "table"

    name: Mapped[str] = mapped_column(nullable=False)
    seats: Mapped[int]
    location: Mapped[str] = mapped_column(nullable=False)

    reservations: Mapped[list["Reservation"]] = relationship(  # type: ignore
        back_populates="table", cascade="all, delete-orphan", passive_deletes=True
    )
