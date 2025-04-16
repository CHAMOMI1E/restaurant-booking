from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Table(Base):
    __tablename__ = "table"

    name: Mapped[str] = mapped_column(nullable=False)
    seats: Mapped[int]
    location: Mapped[str] = mapped_column(nullable=False)
