from datetime import datetime, timedelta
from password import generate_token
from pydantic import BaseModel, EmailStr, Field
from tortoise.models import Model
from tortoise import fields, timezone

def get_expiration_date(duration_seconds: int = 86400) -> datetime:
    return timezone.now() +timedelta(seconds = duration_seconds)

class UserBase(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

class UserDB(User):
    hashed_password: str
"""
We have 3 fields:
* user_id, which will let us identify the user that corresponds to this token
* access_toke, the string that will be passed in the requests to authenticate them. Notice that we defined the generate_token function 
as the default factory. This generates a random secure password, and relies on the standard bsecrets module
* expiration_date, which is the date and time after which the access token will not be valid anymore, here the validity is 24 hours
"""
class AccessToken(BaseModel):
    user_id: int
    access_token: str = Field(default_factory = generate_token)
    expiration_date: datetime = Field(default_factory = get_expiration_date)

    class Config:
        orm_mode = True

class UserTortoise(Model):
    id = fields.IntField(pk=True, max_length = 255)
    email = fields.CharField(index=True, unique=True, null=False, max_length=255)
    hashed_password = fields.CharField(null=False, max_length=255)

    class Meta:
        table='users'
"""
We will create a database access token. This should be a data string that uniquely identifies a user that is impossible to forge by a 
malicious third party. In this example, we'' generate a random string and store it in a dedicated table in our database, witha  foreign
key that refers to every user.
This way, when an authenticated request arrives, we simply have to check whether it exists in the database and look for the corresponding user.
The advantage of this approach is if they are compromised; we only need to delete them from the database

"""

class AccessTokenTortoise(Model):
    access_token = fields.CharField(pk=True, max_length=255)
    user = fields.ForeignKeyField("models.UserTortoise", null=False)
    expiration_date = fields.DatetimeField(null=False)

    class Meta:
        table = 'access_tokens'