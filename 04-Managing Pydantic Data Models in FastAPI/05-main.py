"""
We saw a case where we needed to define two variations of a pydantic model in order to split
 between the data we want to store in the backend and the data we want to show to the user.
 This is a common pattern in FastAPI: you define one model for creation, one for the 
 response and one for the data to store in the database
"""

from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class PostPublic(BaseModel):
    id: int
    title: str
    content: str

class PostDB(BaseModel):
    id: int
    title: str
    content:str
    nb_views: str


"""
We have three models covering 3 situations:
* PostCreate will be used for a a post endpoint to create a new post. We expect the user to
give the title and content; however, the identifier(ID) will be automatically determined by
 the system
* PostPublic will be used to retrieve the data of a post. We want its title and content, 
of course, but also it's asscociated Id in the database
* PostDB will carry all the data we wish to store in the database. Here, we also want to
 store the number of views, but we want to keep this secret to make our own statistics
 internally

To avoid repeating ourseleves, we will use model inheritance to do this. We do this by 
identifying the fields that are common to every other variation and put them in a model that 
will be used as a base for every other. Then you only have to inherit from that model to
create your variations and add the specific fields.
"""

class PostBase(BaseModel):
    title: str
    content: str

    def excerpt(self) -> str:
        return f"{self.content[:140]}..."

class PostCreate(PostBase):
    pass

class PostPublic(PostBase):
    id: int

class PostDB(PostBase):
    id: int
    nb_views: int = 0

"""
Now whenever you need to add a field for the whole entity, all you need to do is add it to 
the PostBase model. It is also very convenient if you wish to define methods to your model.

"""



