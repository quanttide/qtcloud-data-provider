"""
Unittests for dataset endpoints
"""
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


def test_delete_dataset():
    """
    Test delete dataset
    """
    # not found
    response = client.delete('/datasets/test/')
    assert response.status_code == 404
