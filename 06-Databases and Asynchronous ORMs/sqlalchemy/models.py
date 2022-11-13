from datetime import datetime
from typing import Optional

import sqlalchemy
from pydantic import BaseModel, Field
from sqlalchemy import Column, Table, String, Text, DateTime, Integer

class PostBase(BaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)

class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostDB(PostBase):
    id: int

# metadata keeps all tyhe information of a database schema together. Therefore create one and use it in your entire project
metadata = sqlalchemy.MetaData()

posts = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('publication_date', DateTime(), nullable=False),
    Column('title', String(length=255), nullable=False),
    Column('content', Text(), nullable=False)

 )