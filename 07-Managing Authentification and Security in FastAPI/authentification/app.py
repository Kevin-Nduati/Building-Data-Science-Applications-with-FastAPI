"""
We have to create a proper registration route. One thing we have to remember is to hash the password before inserting it  into our database.

"""

from typing import cast
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise import timezone
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist, IntegrityError
from authentication import authenticate, create_access_token
from models import AccessTokenTortoise, User, UserCreate, UserDB, UserTortoise
from password import generate_password_hash


app = FastAPI()

async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl = "/token")),) -> UserTortoise:
    try:
        access_token: AccessTokenTortoise = await AccessTokenTortoise.get(
            access_token = token, expiration_date__gte = timezone.now()
        ).prefetch_related('user')
        return cast(UserTortoise, access_token.user)
    except DoesNotExist:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED
        )
"""
We will call get_password_hash on the input password before inserting the user into the database thanks ti tortoise. Note that we are catching a
possible integrityerror exception which means we areb trying to add an email that already exists. Also notice that we took care to return the 
User model, not the UserDB model. By doing this, we're ensuring that hashed_password is not part of the output. Even hashed, it's generally not
 advisable to leak it.
"""
@app.post("/register", status_code = status.HTTP_201_CREATED)
async def register(user: UserCreate) -> User:
    hashed_password = generate_password_hash(user.password)
    try:
        user_tortoise = await UserTortoise.create(
            **user.dict(), hashed_password = hashed_password
        )
    except IntegrityError:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, detail = "Email Already Exists"
        )
    return User.from_orm(user_tortoise)
"""
When we thinnk of the login endpoint it's goal is to take credentials in the request payload, retrieve the corresponding user, check the password,
and generate a new access token. Its implementation is quite straightforward apart from one thingf: the model that is used to handle the request.

"""
@app.post("/token")
async def create_token(
    form_date: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)
):
    email = form_data.username
    password = form_data.password
    user = await authenticate(email, password)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED
        )
    token = await create_access_token(user)
    return {"access_token": token.access_token, "token_type": "bearer"}


@app.get("/protected-route", response_model = User)
async def protected_route(user: UserDB = Depends(get_current_user)):
    return User.from_orm(user)


TORTOISE_ORM = {
    "connections": {"default": "sqlite://chapter7_authentication.db"},
    "apps": {
        "models": {
            "models": ["chapter7.authentication.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
}

register_tortoise(
    app,
    config = TORTOISE_ORM,
    generate_schemas = True,
    add_exception_handlers = True
)