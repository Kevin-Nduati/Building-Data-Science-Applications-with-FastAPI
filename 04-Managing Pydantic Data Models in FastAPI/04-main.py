"""
Pydantic provides some classes to use as field types to validate some common patterns
such as email addresses or Urls. In the following example, we will use EmailStr and 
HTTPUrl to validate an email address and a http url
"""

from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

class User(BaseModel):
    email: EmailStr
    website: HttpUrl

try:
    User(email='jdoe@example.com', website= "https://www.example.com")
except ValidationError as e:
    print(str(e))