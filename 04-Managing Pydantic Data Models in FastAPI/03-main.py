"""
## Field Validation
Previously, we showed how  to apply some validation to the request parameters to check if a number
was in a certain range or if a string was matching a regex. Actually, those options directly
come from pydantic. To do this, we''ll use the Field function from pydantic and use its
result as the default value of the field. In the following example, wedefine a Person modek with the 
first_name and last_name required properties, which should be at least 3 characters long, and an optional
 age property
"""

from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import List


"""
Pydantic provides the default_factory argument on the Field function to cover the use case
This argument expects you to pass a function that will be called during model instantiation.
Thus, the resulting object will be evaluated at runtime each time you create a new object.
"""
def list_factory():
    return ["a", "b", "c"]

class Model(BaseModel):
    1: List[str] = Field(default_factory = list_factory)
    d: datetime = Field(default_factory = datetime.now)
    12: List[str] = Field(default_factory = list)

"""
You simply have to pass a function to this argument. Don't put arguments on it - it'll be
Pydantic that will automatically call the function for you when instantiating a new object.

"""


