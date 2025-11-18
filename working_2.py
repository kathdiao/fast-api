from fastapi import FastAPI, Path

app = FastAPI()

#   PATCH PARAMETER AND QUERY PARAMETER

inventory = {
    1: {
        "name": "milk",
        "price": 3.98,
        "brand": "Bear brand"
    }
}

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
def get_item( name: str = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

#   = None - optional(hindi required)
