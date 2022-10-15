from fastapi import FastAPI

app = FastAPI()
@app.get("/users")
async def get_user(page: int=1, size: int=10):
    return {"page": page, "size": size}


"""
Query parameters are a common way to add some dynamic parameters to a URL. You find them at the 
end of the URL in the following form: ?param1=foo&param2=bar. In a REST API, they are commonly used
on read endpoints to apply pagination, a filter, a sorting order, or selecting fields. You
simply have to declare them as arguments of your path operation function. If they do not appear 
in the path pattern, as they do for path parameters, FASTAPI automatically considers them to be
 query parameters. """