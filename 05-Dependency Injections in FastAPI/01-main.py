"""
Dependency injection is a system able to automatically instantiate objects and the ones they
depend on. The responsibility of developers is then to only provide a declaration of how an object
should be created, and let the system resolve all the dependency chains and create the actual
objects at runtime

In the following function, we use the header function to retrieve the user-agent header
"""

from typing import Tuple

from fastapi import FastAPI, Depends, Query, Header
app = FastAPI()
@app.get('/')
async def header(user_agent: str = Header(...)):
    return {"user_agenet": user_agent}

"""
Internally, the header function has some logic to automatically get the request object, check for
the required header, return its value, or raise an error if it's not present. From the developer's
perspective, however, we don't know how it handled the required objects for this operation; 
we just ask for the value we need. That''s dependency injection

Admittedly, you could reproduce this example quite easily in the function body by picking 
the user-agent property in the headers dictionary of the Request object. However, the 
dependency injection approach has numerous advantages over this
1. The intent is clear: you know what the endpoint expects in the request data without 
    reading the function's code
2. You have a clear separation concern between the logic of the endpoint and the more
 generic logic: the header retrieval and the associated error handling doesn't pollute the
  rest of the logic; it's self-contained in the dependency function. Besides, it can be
  reused easily in other endpoints
3. In the case of FastAPI, it's used to generate the OpenAPI schema so that the automatic
 documentation can clearly shows which parameters are expected for this endpoint
"""

""" 
## Creating and Using a Function Dependency
A dependency can be defined either as a function or as a callable class. 
Let us look at an example where we define a function dependency to retrieve the pagination
query parameters, skip and limit
"""

async def pagination(skip: int=5, limit: int=10) -> Tuple[int, int]:
    return (skip, limit)

@app.get('/items')
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

"""
There are two parts of this example:
* First, we have the dependency definition, with the pagination function. You see that we
    define two arguments, skip and limit, which are integers with default values. Those will be 
    the query parameters on our endpoint. We define them exactly like we would have done on
    a path operation function. FastAPI will recursively handle the arguments on the dependency
    and match them with the request data
* Secondly, we have the path operation function, list_items, that uses the pagination dependency
    In the case of a dependency, we use the Depends function. Its role is to take a function in 
    the argument and execute it when the endpoint is called
"""