"""
## Appplying validation before pydantic parsing

By default, your validators are run after pydantic has done parsing work. This means that the value
you get already conforms to the type of field you specified. If the type is incorrect, pydantic
raises an error without calling your validator.
However, you may sometimes wish to provide some custom parsing logic that allows yoy to transform 
input values that would have been incorrect for the type you set. In that case, you would need 
to run your validator before the pydantic parser: this is the purpose of the pre argument on
validator
"""

from typing import List
from pydantic import BaseModel, validator

class Model(BaseModel):
    values: List[int]
    @validator('values', pre=True)
    def split_string_values(clas, v):
        if isinstance(v, str):
            return v.split(",")
        return v