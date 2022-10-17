"""
## Raising HTTP Errors
When calling a REST API, quite frequently, you might find that things don't go very well;
you might come across the wrong parameters, invalid payloads.
To raise an HTTP error in FastAPI, you'll have to raise a Python exception, HTTPException.
This exception class will allow us to set a status code and an error code. It is caught by FASTAPI error handlers 
that can take care of forming a proper HTTP response.
In the following example, we will raise a 400 Bad Request Error if the password and password_Confirm 
payload properties don't match
"""
from fastapi import FastAPI, Body, status, HTTPException

app = FastAPI()


@app.post('/password')
async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail = "PAsswords Do not Match"
        )
    return {"message": "Passwords match"}