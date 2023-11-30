"""
Test CRUDs for dataset
"""
from app.cruds.dataset import create_dataset
from app.dependencies.db import BaseORM, Session, engine
from app.orms import DataSetORM
from app.schemas import DataSet

BaseORM.metadata.create_all(bind=engine)


def test_create_dataset():
    """
    Test create dataset
    """
    session = Session()
    dataset = DataSet(name='test', verbose_name='测试数据集', readme='这是一个测试数据集')
    created_dataset = create_dataset(session, dataset)
    retrieved_dataset = session.query(DataSetORM)\
        .filter(DataSetORM.id == created_dataset.id).first()
    assert retrieved_dataset is not None
    assert retrieved_dataset.name == 'test'
    assert retrieved_dataset.verbose_name == '测试数据集'
    assert retrieved_dataset.readme == '这是一个测试数据集'
    session.close()
