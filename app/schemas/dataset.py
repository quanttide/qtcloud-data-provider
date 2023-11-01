from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class DataSet(BaseModel):
    id: UUID
    name: str
    verbose_name: str
    readme: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
