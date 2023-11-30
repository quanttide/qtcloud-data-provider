"""
ORM for dataset
"""
from datetime import datetime

from fastapi_restful.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, DateTime, String, Text

from app.dependencies.db import BaseORM


class DataSetORM(BaseORM):
    """
    ORM for DataSet
    """
    # pylint: disable=R0903
    # Too few public methods
    __tablename__ = 'dataset'

    id: Column[GUID] = Column(GUID, primary_key=True, index=True,
                              default=GUID_DEFAULT_SQLITE)
    created_at: Column[datetime] = Column(DateTime, default=datetime.now)
    updated_at: Column[datetime] = Column(DateTime, default=datetime.now,
                                          onupdate=datetime.now)
    name: Column[str] = Column(String(255), nullable=False, index=True)
    verbose_name: Column[str] = Column(String(255), nullable=True)
    readme: Column[str] = Column(Text, nullable=True)
