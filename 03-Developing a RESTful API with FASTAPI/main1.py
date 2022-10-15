"""
The API path is the main thing that the end user will interact with. Therefore, it's a good spot for
 dynamic parameters. A typical way is to put the unique identifier as an object we want
 to retrieve, such as /users/123. This is how to do it

"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/users/{id}')
async def get_user(id: int):
    return {"id": id}

"""
In this example, we defined an API that expects an integer in the last part of its path. We did
this by putting the parameter name in the path around the curly braces. Then, we defined this
same parameter as an argument for our path operation function. Notice, we add a type hint to specify
the parameter is an integer.
"""