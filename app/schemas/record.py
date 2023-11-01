from uuid import UUID
from pydantic import BaseModel


class DataRecord(BaseModel):
    id: UUID

    class Config:
        orm_mode = True
