"""
Entry module
"""

from fastapi import FastAPI

from .routers import dataset, record, schema

app = FastAPI()
app.include_router(dataset.router)
app.include_router(schema.router)
app.include_router(record.router)


@app.get('/')
async def root():
    """
    Root endpoint.
    """
    return {'msg': 'Hello World!'}
