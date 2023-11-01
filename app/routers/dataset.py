from fastapi import APIRouter

router = APIRouter(prefix="/datasets", )


@router.get("/")
async def list_datasets():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/")
async def create_dataset():
    return {"username": "Rick"}


@router.get("/{name}")
async def retrieve_dataset(name: str):
    return {"username": name}


@router.put("/{name}")
async def update_dataset(name: str):
    return {"username": name}


@router.patch("/{name}")
async def patch_dataset(name: str):
    return {"username": name}


@router.delete("/{name}")
async def delete_dataset(name: str):
    return {"username": name}
