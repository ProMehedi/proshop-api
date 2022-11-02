import os

SECRET_KEY = os.environ.get('SECRET_KEY')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
MONGO_URI = os.environ.get('MONGO_URI')
URL_PREFIX = os.environ.get('URL_PREFIX')