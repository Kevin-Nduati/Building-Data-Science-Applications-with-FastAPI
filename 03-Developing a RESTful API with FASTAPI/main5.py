"""
If you wish to define a required query parameter, simply leave out the default value"""
from enum import Enum
from fastapi import FastAPI

class userFormat(str, Enum):
    SHORT = 'short'
    FULL = 'full'

app = FastAPI()
@app.get("/users")
async def get_user(format: userFormat):
    return {"format": format}

"""
If you omit the format parameter in the URL, you will get a 422 error response. Additionally,
notice that we defined UserFormat enumeration to limit the number of allowed values for this
parameter"""