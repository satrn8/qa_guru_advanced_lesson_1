from fastapi import FastAPI, HTTPException
from typing import List
from models import Item

app = FastAPI()

items = []


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    item.id = len(items) + 1
    items.append(item)
    return item


@app.get("/items/", response_model=List[Item])
def read_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for item in items:
        if item.id == item_id:
            item.name = updated_item.name
            item.description = updated_item.description
            item.price = updated_item.price
            item.tax = updated_item.tax
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return item
    raise HTTPException(status_code=404, detail="Item not found")
