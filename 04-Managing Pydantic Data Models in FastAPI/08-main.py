"""
## Working with Pydantic Models

When developing API endpoints with FastAPI, you'll likely get a lot of Pydantic model
instances to handle. It's then up to you to implement the logic to make a link between
those objects and your services, such as your database or your ML model

### Converting an object into a dictionary
The following example reuses the Person and Address models we saw
"""

from datetime import date
from enum import Enum
from typing import List
from pydantic import BaseModel

class Gender(str, Enum):
    MALE= 'MALE'
    FEMALE= 'FEMALE'
    NON_BINARY= 'NON_BINARY'

class Address(BaseModel):
    street_address: str
    postal_code: str
    city:str
    country:str

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address

person = Person(
    first_name = "John",
    last_name = 'Doe',
    gender = Gender.MALE,
    birthdate = "1990-01-01",
    interests = ['travel', 'swimming'],
    address = {
        "street_address": "12 Squirrel",
        "postal_code": "2772",
        "city": "Nairobi",
        "country": "Kenya"
    }
)

person_dict = person.dict()
print(person_dict['first_name'])
print(person_dict['address']['street_address'])


""""""
