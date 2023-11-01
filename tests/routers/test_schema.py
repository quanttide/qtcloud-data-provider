import pytest
from app.routers.dataset import *
from app.schemas import DataSchema


@pytest.fixture
def test_create_data_schema():
    dataset = create_dataset()
