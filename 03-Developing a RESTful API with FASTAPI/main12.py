"""
## Setting headers
This only involves setting the proper type hinting to the argument. The following
exaample shows you how to set a custom header
"""

from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def custom_header(response: Response):
    response.headers['Custom-Header'] = "Custome-Header-Value"
    return {"hello": "world"}

"""
The Response object gives you access to a set of properties, including headers. It's a simple
dictionary where the ley is the name of the header, and the value is its associated value. 
You also do not have to return the Response object. You can still return JSON-encodable data 
and FastAPI will take care of forming a proper response, including the headers that you have set"""