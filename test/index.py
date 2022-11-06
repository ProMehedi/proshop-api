import simplejson
import json
from pydantic import BaseModel, ValidationError, validator
from email_validator import validate_email, EmailNotValidError
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type


# class UserModel(BaseModel):
#     name: str
#     username: str
#     password: str

#     @validator('name')
#     def name_must_contain_space(cls, v):
#         if ' ' not in v:
#             raise ValueError('must contain a space')
#         return v.title()

#     @validator('username')
#     def username_alphanumeric(cls, v):
#         assert v.isalnum(), 'must be alphanumeric'
#         return v

#     @validator('password')
#     def password_length(cls, v):
#         assert len(v) >= 8, 'must be at least 8 characters'
#         return v


# # user = UserModel(
# #     name='samuel colvin',
# #     username='scolvin',
# #     password='zxcvbn',
# # )
# # print(user)

# try:
#     UserModel(
#         name='samuel',
#         username='scolvin',
#         password='zxcvbn',
#     )
# except ValidationError as e:
#     print(e)


# try:
#     valid = validate_email("test@gmail.com")
#     email = valid.email
#     print(email)
# except EmailNotValidError as e:
#     print(e)


# number = "+880178292"
# valid = carrier._is_mobile(number_type(phonenumbers.parse(number)))
# print(valid)

# user = {'_id': '6362cd8f5d97edcf89a23a70',
#         'first_name': 'Mehedi', 'last_name': 'Hasan',
#         'email': 'mehedi@example.com', 'phone': '+8801782927925',
#         'password': 'pbkdf2:sha256:260000$jtCKC8nQEDWX1o88$d22ff9d2b8f03e631d19704482e287a622aa1a6fe08559f0141bbb4c247d6ff9', 'role': 'admin', 'created_at': '2021-05-09 12:00:00'}

# # Remove password from user dict
# user.pop('password')
# print(user)

# new_user = dict(user).pop('password')
# print(new_user)

from pydantic import BaseModel, Field, constr, conint, confloat
from typing import List
import os
import pymongo
from bson.objectid import ObjectId
import datetime as dt


class Review(BaseModel):
    name: str
    rating: int = Field(ge=1, le=5)
    comment: str


class Product(BaseModel):
    name: str
    price: float = Field(ge=0)
    reviews: List[Review] = []


client = pymongo.MongoClient(
    'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0')
db = client['proshop']

product = Product(name='test', price=100.00)
review = Review(name='test', rating=5, comment='test')

# created_product = db.products.insert_one(dict(product))
# created_review = db.reviews.insert_one(dict(review))

# db.products.find_one_and_update({'_id': created_product.inserted_id}, {
#     '$push': {'reviews':  ObjectId(created_review.inserted_id)}})

# db.reviews.find_one_and_update({'_id': created_review.inserted_id}, {
#     '$set': {'product': ObjectId(created_product.inserted_id)}})

# new_review = db.reviews.insert_one(dict(review))
# db.products.find_one_and_update({'_id': ObjectId('6366dde205467979d841ab1c')}, {
#     '$push': {'reviews': ObjectId(new_review.inserted_id)}})

# Get the product with reviews
product = db.products.find_one({'_id': ObjectId('6366dde205467979d841ab1c')})

# Get the reviews
if product:
    reviews = db.reviews.find({'_id': {'$in': product['reviews']}})
    product['reviews'] = list(reviews)

result = json.loads(simplejson.dumps(product, ignore_nan=True, default=str))
print(json.dumps(result, indent=2))
