"""
## The Response Model
With FastAPI, the main use case is to directly return a pydantic model that automatically
gets turned into a properly formatted JSON. However, quite often, you'' find that there are 
some differences between the input data, the data  you store in your database, and the data 
you want to show to the end user. For instance, perhaps some fields are private or only for
internal use, or perhaps some fields are only useful during the creation process and then
discarded afterwards.
Asssume you have a database containing blog posts. Those blog posts have several properties
such as title, content, or creation date. Additionally, you store the number of views of each one, 
but you do not want the end user to see any of this
"""

from fastapi import FastAPI
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

app = FastAPI()

# Dummy database
posts = {
    1: Post(title='Hello', nb_views=100),
}

@app.get('/posts/{id}')
async def get_post(id: int):
    return posts[id]