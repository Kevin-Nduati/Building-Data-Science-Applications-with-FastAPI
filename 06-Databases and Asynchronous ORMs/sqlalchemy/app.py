from typing import List, Tuple

from databases import Database
from fastapi import Depends, FastAPI, HTTPException, Query, status

from database import get_database, sqlalchemy_engine
from models import metadata, posts, PostDB, PostCreate, PostPartialUpdate

app = FastAPI()

@app.on_event('startup')
async def startup():
    await get_database().connect()
    metadata.create_all(sqlalchemy_engine)

@app.on_event('shutdown')
async def shutdown():
    await get_database().disconnect()

"""
Decorating with the on_event decorators allows us to trigger some useful logic when fastapi starts or stops
In this case, we simply call the connect and disconnect methods of a database accordingly. 
We also call the create_all method on the metadata. This is important as to create a table's schema inside our database
"""

### Making Insert Queries
"""
Let us start with the insert queries to create new rows in our database
We create a post endpoint that accepts a payload following the PostCreate model. It also injects
into our database thanks to the get_database dependency

"""
async def get_post_or_404(id: int, database: Database = Depends(get_database)) -> PostDB:
    select_query = posts.select().where(posts.c.id == id)
    raw_post = await database.fetch_one(select_query)

    if raw_post is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    return PostDB(*raw_post)


@app.post('/posts', response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, database: Database = Depends(get_database)) -> PostDB:
    insert_query = posts.insert().values(post.dict())
    post_id = await database.execute(insert_query)

    post_db = await get_post_or_404(post_id, database)
    return post_db

