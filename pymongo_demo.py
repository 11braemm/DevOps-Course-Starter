import os
import dotenv
import pymongo

dotenv.load_dotenv()

connection_string = os.getenv("MONGODB_CONNECTION_STRING")

client = pymongo.MongoClient(connection_string)

db = client.emmbramongodb

collection = db.todo_items

# Add document
# collection.insert_one({"description": "play table football"})

# Get list of documents
# list(collection.find())

# Update document 
# collection.update_one({"type": "updateable"}, {"$set": {"description": "Changed"}})


print(list(collection.find()))
