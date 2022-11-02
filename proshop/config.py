import pymongo
from .settings import MONGO_URI

client = pymongo.MongoClient(MONGO_URI)
db = client['proshop']
