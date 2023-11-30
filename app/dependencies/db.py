"""
Database with sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 使用内存作为SQLite数据库，不创建真实数据库文件
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///:memory:'

# SQLAlchemy DB Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
# ORM Session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# pylint: disable=R0903
# Too few public methods
class BaseORM(DeclarativeBase):
    """
    Base ORM
    """
