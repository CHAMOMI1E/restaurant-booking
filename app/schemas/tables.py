from pydantic import BaseModel, ConfigDict, Field, field_validator


class TableBase(BaseModel):
    name: str
    seats: int = Field(..., gt=0)
    location: str


class TableCreate(TableBase):
    pass


class Table(TableBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
