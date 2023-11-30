"""
Base classes for pydantic schemas.
"""
from typing import Annotated
from uuid import UUID, uuid4

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field


class BaseModel(PydanticBaseModel):
    """
    BaseModel with default fields.
    """

    id: Annotated[UUID, Field(default_factory=uuid4, frozen=True)]
    # created_at: Annotated[datetime,
    # Field(default_factory=datetime.utcnow, frozen=True)]
    # updated_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]
    # created_by: Annotated[UUID, Field(default=None)]
    # updated_by: Annotated[UUID, Field(default=None)]
