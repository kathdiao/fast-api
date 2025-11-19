from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
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
def get_item(name: str = None):
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