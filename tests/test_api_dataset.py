"""
Unittests for dataset endpoints
"""
import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_datasets():
    """
    Test list datasets
    :return:
    """
    response = client.get('/datasets/')
    assert response.status_code == 200
    assert response.json() == []


def test_create_dataset():
    """
    Test create dataset
    :return:
    """
    dataset_data = {
        'id': str(uuid.uuid4()),
        'name': 'test',
        'verbose_name': '测试数据集',
        'readme': '这是一个测试数据集',
    }
    response = client.post('/datasets/', json=dataset_data)
    assert response.status_code == 201
    assert response.json() == dataset_data


def test_delete_dataset():
    """
    Test delete dataset
    """
    # not found
    response = client.delete('/datasets/test/')
    assert response.status_code == 404
