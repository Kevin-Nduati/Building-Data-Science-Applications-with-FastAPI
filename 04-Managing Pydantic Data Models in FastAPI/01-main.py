from datetime import date
from enum import Enum
from typing import List
from pydantic import BaseModel, ValidationError

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address

"""
We used the standard Python Enum class as a type for the gender field. This allows us to specify
a set of valid values. If we input a value that is not in the enumeration, pydantic will
raise an error
"""

try:
    Person(
        first_name="John",
        last_name='Doe',
        gender = "MALE",
        birthdate = "1991-01-01",
        interests = ['travel', 'swimming'],
        address = {
            "street_address": "155366",
            "postal_code": "2661",
            "city": "Nairobi",
            "country": "Kenya"
        }
    )
except ValidationError as e:
    print(str(e))