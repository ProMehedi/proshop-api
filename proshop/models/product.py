from pydantic import BaseModel, Field, constr
from typing import List, Any
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


class Brand(BaseModel):
    name: str
    slug: str
    desc: str
    image: str
    status: Status
    createdAt: str = Field(default=dt.datetime.utcnow())
    updatedAt: str


class Product(BaseModel):
    name: str = Field(min_length=3, strip_whitespace=True, strict=True)
    slug: constr(strip_whitespace=True, strict=True)
    desc: str = Field(min_length=10, default="")
    shortDesc: constr(min_length=10, strip_whitespace=True,
                      strict=True, curtail_length=100) = Field(default=None)
    price: float = Field(ge=0.0, default=0.0)
    regularPrice: float = Field(ge=0.0, default=None)
    categories: list = Field(default=[])
    type: Type = Field(default=Type.simple)
    status: Status = Field(default=Status.draft)
    featured: bool = False
    stockQuantity: int = Field(ge=0, default=0)
    sku: constr(min_length=3, strip_whitespace=True,
                strict=True) = Field(default=None)
    thumbnail: str = ""
    images: list = Field(default=[])
    attributes: list = Field(default=[])
    brand: Brand = Field(default=None)
    rating: float = Field(ge=0.0, le=5.0, default=None)
    createdAt: str = Field(default=dt.datetime.utcnow())
    updatedAt: str = ""
    userId: Any
    reviews: List[Review] = []
