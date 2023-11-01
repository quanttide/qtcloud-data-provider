from uuid import UUID
from pydantic import BaseModel


class DataSchema(BaseModel):
    id: UUID

    class Config:
        orm_mode = True
