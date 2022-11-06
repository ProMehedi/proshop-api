from pydantic import BaseModel, Field, constr
from typing import List
from enum import Enum
import datetime as dt


class Type(str, Enum):
    simple = 'simple',
    grouped = 'grouped'
    external = 'external'
    variable = 'variable'


class Status(str, Enum):
    draft = 'draft'
    pending = 'pending'
    private = 'private'
    publish = 'publish'


class Review(BaseModel):
    name: str
    rating: float = Field(ge=1, le=5)
    comment: str
    reviewBy: str
    reviewFor: str


class Product(BaseModel):
    name: str = Field(min_length=3, strip_whitespace=True, strict=True)
    slug: constr(strip_whitespace=True, strict=True)
    desc: str = Field(min_length=10, default="")
    shortDesc: constr(min_length=10, strip_whitespace=True,
                      strict=True, curtail_length=100) = ""
    price: float = Field(ge=0.0, default=0.0)
    regular_price: float = Field(ge=0.0, default=None)
    category: str = ""
    type: Type = Type.simple
    status: Status = Status.publish
    featured: bool = False
    quantity: int = Field(ge=0, default=0)
    sku: constr(min_length=3, strip_whitespace=True, strict=True) = None
    images: list = Field(default=[])
    attributes: list = Field(default=[])
    categories: list = Field(default=[])
    rating: float = Field(ge=0.0, le=5.0, default=None)
    created_at: str = Field(default=dt.datetime.utcnow())
    updated_at: str = ""
    user_id: str
    reviews: List[Review] = []
