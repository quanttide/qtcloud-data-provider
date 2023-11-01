from datetime import datetime
from fastapi_restful.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, String, Text, DateTime


class Id(GUID):
    pass


class Name(String):
    pass


class VerboseName(String):
    pass


class Description(String):
    pass


class Readme(String):
    pass


class CreatedAt(DateTime):
    pass


class UpdatedAt(DateTime):
    pass
