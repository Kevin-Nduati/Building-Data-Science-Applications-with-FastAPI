"""
## Use a dependency on a whole router

You can create several routers in your project to clearly split the different parts of your API
and wire them to your main FastAPI application. This is done with the APIRouter class and the 
include_router method 
With this approach, it can be interesting to inject a dependency on the whole router, so thta it
is called for every route of this router.
There are 2 ways of doing this:
* Set the dependencies argument on the APIRouter class as follows:
"""


from typing import Optional
from fastapi import APIRouter, FastAPI, Depends, Header, HTTPException, status

def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)


router = APIRouter(dependencies = [Depends(secret_header)])

@router.get("/route1")
async def router_route1():
    return {"route": "route1"}

@router.get("/route2")
async def router_route2():
    return {"route": "route2"}

app = FastAPI()
app.include_router(router, prefix="/router")


"""
In both cases, the dependencies argument expects a list of dependencies. You see, just  
like for dependencies you pass in the arguments, you need to wrap your function with 
the Depends function. Of course, since it's a list, you can add several dependecies
if you need

Now, how to choose between the two approaches. In both cases, the effect will be exactly
the same, so we could say it doesn't really matter. 
"""