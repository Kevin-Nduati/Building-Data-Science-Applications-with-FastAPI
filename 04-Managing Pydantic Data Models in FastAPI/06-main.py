"""
## Addit Custom Data Validation with Pydantic
We've seen how to apply basic validation to our models, through the Field arguments or 
the custom types provided by pydantic. Pydantic allows this by defining validators, which
 are methods on the model that can be applied at a field level or an object level

### Applying validation at a field level
This is the most common case: have a validation rule for a single field. To define it 
with pydantic, we'll just have to write a static method on our model and decorate it witj
the validator decorator. As a reminder, decorators are syntactic sugar, allowing the wrapping
of a function or a class with common logic, without compromising readability

"""
from datetime import date
from pydantic import BaseModel, validator

class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @validator('birthdate')
    def valid_birthdate(cls, v:date):
        delta = date.today() - v
        age = delta.days /365
        if age >  120:
            raise ValueError('You seem a bit too old')
        return v

"""
The validator is a static class method(with first argument, cls, being the class itself), with
the value to validate as the v argument. It's decorated by the validator decorator, which expects the
name of the argument to validate as the first argument
Pydantic expects two things for this method, detailed as follows:
* If the value is not valid, you should raise a valuerror with an explicit message
* Otherwise, you should return the value that will be assigned in the model
"""

"""
## Applying validation at an object level
It happens quite often that the validation of one field is dependent on another - for example
to check if a password conformation matches the password or to enforce a field to be required 
in certain circumstances. To allow this kind of validation, we need to acces sthe whole object 
data. 
"""
from pydantic import BaseModel, EmailStr, ValidationError, root_validator

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @root_validator()
    def passwords_match(cls, values):
        password = values.get('password')
        password_confirmation = values.get('password_confirmation')
        if password != password_confirmation:
            raise ValueError('Passwords do not match')
        return values


"""
The use of this decorator is similar to the validator decorator. The static class method is 
called along with the values argument, whic is a dictionary containing all the fields. Thus,
you can retrieve each one of them and implement your logic

"""