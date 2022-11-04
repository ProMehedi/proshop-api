from pydantic import BaseModel, Field, constr, conint, confloat
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


class Product(BaseModel):
    name: constr(min_length=3, strip_whitespace=True, strict=True)
    slug: constr(strip_whitespace=True, strict=True)
    desc: str = None
    short_desc: constr(min_length=10, strip_whitespace=True,
                       strict=True, curtail_length=100)
    price: confloat(ge=0.0)
    regular_price: confloat(ge=0.0) = None
    category: str = None
    type: Type = Type.simple
    status: Status = Status.publish
    featured: bool = False
    quantity: conint(ge=0)
    sku: constr(min_length=3, strip_whitespace=True, strict=True) = None
    images: list = Field(default=[])
    attributes: list = Field(default=[])
    categories: list = Field(default=[])
    rating: confloat(ge=0.0, le=5.0) = 0.0
    created_at: str = Field(default=dt.datetime.utcnow())
    updated_at: str = None
    user_id: str
