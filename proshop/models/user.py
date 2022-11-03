from pydantic import BaseModel, Field, ValidationError, validator, EmailStr, constr
from enum import Enum
from typing import Any, List, Tuple, Union
from email_validator import validate_email, EmailNotValidError
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import datetime as dt


class Role(str, Enum):
    admin = 'admin'
    customer = 'customer'
    marchant = 'marchant'


class Address(BaseModel):
    address: str
    city: str
    state: str = None
    country: str = None
    zip: constr(min_length=4, max_length=6) = None


class User(BaseModel):
    firstName: constr(min_length=2, strip_whitespace=True,
                      strict=True, curtail_length=25)
    lastName: constr(strip_whitespace=True, strict=True,
                     curtail_length=25) = None
    email: EmailStr = Field(...)
    phone: constr(min_length=8, max_length=15, strip_whitespace=True)
    password: str = Field(min_length=8)
    role: Role = Role.customer
    created_at: str = Field(default=dt.datetime.utcnow())
    address: dict = None

    @validator('email')
    def email_must_be_valid(cls, v):
        try:
            valid = validate_email(v)
            email = valid.email
            return email
        except EmailNotValidError as e:
            raise ValueError(e)

    @validator('phone')
    def phone_must_be_valid(cls, v):
        valid = carrier._is_mobile(number_type(phonenumbers.parse(v)))
        if not valid:
            raise ValueError('Invalid phone number')
        return v
