"""
CURDs for DataSet
"""
from sqlalchemy.orm import Session

from app.orms import DataSetORM
from app.schemas import DataSet


def create_dataset(db: Session, dataset: DataSet) -> DataSetORM:
    """
    create dataset
    :param db:
    :param dataset:
    :return:
    """
    db_dataset = DataSetORM(**dataset.model_dump())
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset
