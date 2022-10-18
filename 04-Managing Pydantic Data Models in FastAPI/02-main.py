"""
## Optional fields and default values
Quite often, however, there are values that we want to be optional because they wmay not 
be relevant for each object instance. Sometimes, we also wish to set a default value 
for a field when it's not specified
"""

from typing import Optional
from pydantic import BaseModel

class UserProfile(BaseModel):
    nickname: str
    location: Optional[str] = "Nairobi"
    subscribed_newsletter: bool = True

user = UserProfile(nickname = "jdoe")
print(user)