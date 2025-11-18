from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    """
    GET /
    Home route
    Returns a simple JSON message
    """
    return {"Data": "Testing"}


# HTTP Methods
#   GET - get something for you and return it
#   POST - you're going to send information to the endpoint or Adding new user to DB
#   PUT - Update something in your database
#   DELETE - Get rid of something

# More:
# Endpoint = route that users/devs can access
# Example: facebook.com/home (home is the endpoint)

# COMMON HTTP STATUS CODES
# 200 - OK (success)
# 201 - Created (resource successfully created)
# 204 - No Content (success but no response body)
# 400 - Bad Request (client-side error)
# 401 - Unauthorized (authentication required or failed)
# 403 - Forbidden (authenticated but not allowed)
# 404 - Not Found (resource does not exist)
# 409 - Conflict (duplicate resource or conflict)
# 422 - Unprocessable Entity (validation error, missing fields)
# 500 - Internal Server Error (server-side error)