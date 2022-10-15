"""
When defining more advanced validation rules, particularly for numbers and strings,
type hinting is no longer enough. We'll rely on the functions provided by fastapi
For path parameters, the function is named Path. In the following example, we'll only
allow an id argument that is greater than or equal to 1
"""
from fastapi import FastAPI, Path
app = FastAPI()

app.get("/users/{id}")
async def get_user(id: int = Path(..., ge=1)):
    return {"id": id}

"""
The result of the Path is used as a default value for the id argument in the path
operation function. We can see the ellipsis syntax as the first parameter of PAth. 
Indeed it expects the default value for the parameter as the first argument. In this
scenario, we don't want a default value: the parameter is required. Therefore, ellipses
are here to tell FastAPI that we don't want a default value"""