from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}

# GET Method
@app.get("/")
def home():
    return {"Data": "Testing"}


#another endpoint/route
@app.get("/about")
def about():
    return {"Data": "About"}


#   PATH PARAMETER AND QUERY PARAMETER


#   PATH PARAM
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="The ID of the Item you want to get.")):
    return inventory[item_id]

# Example URL: facebook.com/home?redirect=/kath&msg=fail
# - endpoint = /home
# - redirect = query parameter key, value = "/kath"
# - msg      = query parameter key, value = "fail"


#   QUERY PARAM
@app.get("/get-by-name")
def get_by_name(name: str = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

#   = None - optional(hindi required)


#   REQUEST BODY AND POST METHOD
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exists"}

    inventory[item_id] = item.model_dump()
    return inventory[item_id]

#   UPDATE METHOD
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item not found"}

    if item.name is not None:
        inventory[item_id]["name"] = item.name

    if item.price is not None:
        inventory[item_id]["price"] = item.price

    if item.brand is not None:
        inventory[item_id]["brand"] = item.brand

    return inventory[item_id]

#   DELETE METHOD
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the Item you want to delete.")):

    if item_id not in inventory:
        return {"Error": "Item not found"}

    del inventory[item_id]
    return {"Success": f"Item {item_id} deleted"}