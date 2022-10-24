"""
## Get an object or raise a 404 error

In a REST API, you'lll typically have endpoints to get, update and delete a single object
given its identifier in the path. On each one, you'll likely have the same logic: try to 
retrieve this object in the database or raise an error 404 if it doesn't exist. That's a 
perfect use case for a dependency
"""

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Optional

class Post(BaseModel):
    id: int
    title: str
    content: str

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]

class DummyDatabase:
    posts: Dict[int, Post] = {}

db = DummyDatabase()

db.posts = {
    1: Post(id=1, title="post 1", content="content 1"),
    2: Post(id=2, title="post 2", content="content 2"),
    3: Post(id=3, title="post 3", content="content 3")
}

app = FastAPI()

async def get_post_or_404(id: int) -> Post:
    try:
        return db.Posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

"""
It takes an argument the ID of the post we want to retrieve. It will be pulled
 from the corresponding path parameter. Then we check whether it exists in our
  dummy dictionary: if it does, we return it, otherwise, we raise an exception.

Another typical way for this is authentification: if the endpoint requires a user to be
authenticated, we raise a 401 error in the dependency by checking for the token or
the cookie

"""

@app.get("/posts/{id}")
async def get(post: Post = Depends(get_post_or_404)):
    return post

@app.patch("/posts/{id}")
async def update(post_update: PostUpdate, post: Post = Depends(get_post_or_404)):
    updates_post = post.copy(update = post_update.dict())
    db.posts[post.id] = updates_post
    return updated_post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post: Post = Depends(get_post_or_404)):
    db.posts.pop(post.id)

"""
As you can see, we just had to define the post argument and use the Depends function on our
get_post_or_404 dependency. Then within the path operation logic, we are guaranteed to have 
our post object at hand and we can focus on our core logic, which is now very concise. Then get 
endpoint, for example, just has to return the object

In this case, the only point of attention is to not forget the ID parameter in the path of those 
endpoints. According to the rules of fastapi, if you don't set this parameter in the path,
it will automatically be regarded as a query parameter, which is not what we want
"""