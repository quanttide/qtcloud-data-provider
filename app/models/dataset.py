from datetime import datetime

from sqlalchemy import Column, String, Text, DateTime
from fastapi_restful.guid_type import GUID, GUID_DEFAULT_SQLITE
from ..dependencies.db import Base


class DataSet(Base):
    __tablename__ = "dataset"

    id = Column(GUID, primary_key=True, index=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String(255), nullable=False, index=True)
    verbose_name = Column(String(255), nullable=True)
    readme = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
