from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb://104.237.3.15:27017/') #replace with mongo IP
db = client.ip_database
collection = db.ip_addresses

# Fetch all documents from the collection
documents = collection.find()

# Print the documents
for doc in documents:
    print(doc)
