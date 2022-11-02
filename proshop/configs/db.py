import pymongo
from .settings import MONGO_URI

# Enable timestamps for the documents
client = pymongo.MongoClient(MONGO_URI, document_class=dict, tz_aware=True)
db = client['proshop']
