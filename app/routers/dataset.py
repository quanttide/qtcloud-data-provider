"""
Dataset Endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.cruds.dataset import create_dataset as create_dataset_crud
from app.dependencies.db import get_db
from app.schemas import DataSet

router = APIRouter(prefix='/datasets')
# In-memory database (for demonstration purposes)
datasets: list[DataSet] = []


@router.get('/')
async def list_datasets():
    """
    list all datasets
    """
    return datasets


@router.post('/', status_code=201, response_model=DataSet)
async def create_dataset(dataset: DataSet, db: Session = Depends(get_db)):
    """
    create a new dataset
    """
    db_dataset = create_dataset_crud(db, dataset)
    return db_dataset


@router.get('/{name}')
async def retrieve_dataset(name: str):
    """
    retrieve dataset by its name
    :param name: dataset name
    :return: dataset
    """
    return {'username': name}


@router.put('/{name}')
async def update_dataset(name: str):
    """
    update dataset by its name
    :param name: dataset name
    :return: dataset
    """
    return {'username': name}


@router.patch('/{name}')
async def partial_update_dataset(name: str):
    """
    partial update dataset by its name
    :param name: dataset name
    :return: dataset
    """
    return {'username': name}


@router.delete('/{name}', status_code=204)
async def delete_dataset(name: str):
    """
    delete dataset by its name
    :param name: dataset name
    :return: None
    """
    # 找到要删除的数据集的索引
    index_to_delete = None
    for i, dataset in enumerate(datasets):
        if dataset.name == name:
            index_to_delete = i
            break

    # 如果找到了要删除的索引，使用 pop 删除
    if index_to_delete:
        datasets.pop(index_to_delete)
        return None
    raise HTTPException(status_code=404, detail=f'Dataset {name} not found')
