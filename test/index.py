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

user = {'_id': '6362cd8f5d97edcf89a23a70',
        'first_name': 'Mehedi', 'last_name': 'Hasan',
        'email': 'mehedi@example.com', 'phone': '+8801782927925',
        'password': 'pbkdf2:sha256:260000$jtCKC8nQEDWX1o88$d22ff9d2b8f03e631d19704482e287a622aa1a6fe08559f0141bbb4c247d6ff9', 'role': 'admin', 'created_at': '2021-05-09 12:00:00'}

# Remove password from user dict
user.pop('password')
print(user)

# new_user = dict(user).pop('password')
# print(new_user)
