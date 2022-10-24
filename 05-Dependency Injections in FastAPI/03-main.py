"""
Dependencies are the recommended way to create building blocks in a fastapi project, allowing
you to reuse logic across endpoints while maintaining maximum code readability. We can expand this across 
the whole project
The main motivation for this is to be able to apply some global request validation or perform
side logic on several routes without the need to add the dependency on each endpoint.
"""

from typing import Optional

from fastapi import FastAPI, Depends, Header, HTTPException, status

app = FastAPI()

def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

"""
This dependency will simply look for a header in the request named Secret-Header. If it 
is missing or not equal to SECRET_VALUE, it will raise a 403 error. 
"""

@app.get("/protected-route", dependencies = [Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}

"""
The path operation decorator accepts an argument, dependencies, which expects a list of 
dependencies. You have to wrap your function with the Depends function. Now, whenever the
/protected-route is called, the dependency will be called and will check for the required 
header. 
"""
