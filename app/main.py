from fastapi import FastAPI, Request

from .routers import dataset

app = FastAPI()
app.include_router(dataset.router)


@app.get("/")
async def root(request: Request):
    return {"Host": request.headers["host"]}
