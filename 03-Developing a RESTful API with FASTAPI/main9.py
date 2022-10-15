"""
Besides the URL and the body, another major part of the HTTP request are the headers.
They contain all sorts of metadata that can be useful when handling requests. A common way 
usage is to use them for authentification, for example via cookies.
Once again, retrievibg them in FastAPI only involves a type hint and a parameter function. 
"""
from fastapi import FastAPI, Header
app = FastAPI()

@app.get('/')
async def get_header(hello: str = Header(...)):
    return {"hello": hello}