from pydantic import BaseModel, Field
import datetime as dt


class User(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    password: str = Field(...)
    role: str = Field(default='customer')
    created_at: str = Field(default=dt.datetime.utcnow())
