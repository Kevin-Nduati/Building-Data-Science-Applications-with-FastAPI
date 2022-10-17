"""
## Setting the status code dynamically
We discussed a way to declaratively set the status code of the response. The drawback
to this approach is that it'll always be the same no matter what is happening inside
LEt us assume that we have an endpoint that updates an object in the database or creates 
it if it does not exist. A good approach would be to return a 200 OK status when the object 
already exists or a 201 CREATED status when the object has to be created
"""
from fastapi import FastAPI, status, Response
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int
app = FastAPI()
## Dummy database
posts = {
    1: Post(title = "Hello", nb_views=100)
}

@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]