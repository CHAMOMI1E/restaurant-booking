from .base import BaseDAO
from app.db.models.tables import Table


class TableDAO(BaseDAO):
    model = Table
