"""
Unittests for dataset router
"""
import pytest

from app.dependencies.db import BaseORM, engine
from app.routers.dataset import create_dataset
from app.schemas import DataSet

BaseORM.metadata.create_all(bind=engine)


@pytest.mark.asyncio
async def test_create_dataset():
    """
    Test create dataset
    :return:
    """
    dataset_data = {
        'name': 'test',
        'verbose_name': '测试数据集',
        'readme': '这是一个测试数据集',
    }
    response_raw = await create_dataset(DataSet(**dataset_data))
    # 模拟FastAPI的框架转换
    response_data = DataSet.model_validate(response_raw).model_dump()
    assert response_data['id'] is not None
    assert response_data['created_at'] is not None
    assert response_data['updated_at'] is not None
    assert response_data['name'] == dataset_data['name']
    assert response_data['verbose_name'] == dataset_data['verbose_name']
    assert response_data['readme'] == dataset_data['readme']
