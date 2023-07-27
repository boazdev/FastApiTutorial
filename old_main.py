""" from typing import Annotated
from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Good bye slavery"}

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results """

""" @app.get("/items/me")
async def read_curr_item():
    return {"item_id":"current item"}

@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip:skip+limit] """

