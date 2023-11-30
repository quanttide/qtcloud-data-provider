"""
Unittests for domain models of DataSet subdomain
"""
from uuid import UUID

from app.schemas import DataSet


def test_dataset():
    """
    Test DataSet domain model
    """
    dataset = DataSet(name='test', verbose_name='测试数据集', readme='这是一个测试数据集')
    assert isinstance(dataset.id, UUID)
    assert dataset.name == 'test'
    assert dataset.verbose_name == '测试数据集'
    assert dataset.readme == '这是一个测试数据集'
