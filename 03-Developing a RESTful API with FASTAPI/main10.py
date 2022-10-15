"""Most of the time, you'll want to customize responses a bit further: for instance, by changing the
the status code, riasing validation errors, and setting cookies. FastAPI offers different ways 
to do this, from the simplest case to the most advanced one. 

"""
"""
## The Status Code
The most obvious thing to customize in an HTTP response is the status code. By default, 
FastAPI will always set a 200 status when everything goes well during your path operation
 function execution. 
 Sometimes it might be useful to change this. For example, it is good practice in a REST 
 API to retuirn a 201 Created Status when the execution of the endpoint
 ends up in the creation of a new object
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str

app = FastAPI()

@app.post("/posts", status_code = status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post