import os
from bson import ObjectId
import pymongo

from todo_app.data.Item import Item


def get_collection():
    """
    Sets up a conection to the MongoDB database and returns the to do collection.
    """
    
    client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))
    db = client[os.getenv("MONGODB_DATABASE_NAME")]
    return db[os.getenv("MONGODB_COLLECTION_NAME")]

def add_item(title: str):
    """
    Adds a new item with the specified title to MongoDB.

    Args:
        title: The title of the item.
    """
    new_to_do = {"status": "Not started", "description": title}
    collection = get_collection()
    collection.insert_one(new_to_do)


def get_items():
    """
    Fetches all saved items from MongoDB.

    Returns:
        list: The list of saved items.
    """
    collection = get_collection()
    mongo_documents = list(collection.find())
    return [Item.from_mongo_document(document) for document in mongo_documents]


def mark_item_as_done(todo_id):
    """
    Marks the MongoDB with the specified ID as done.

    Args:
        card_id: The ID of the MongoDB item to mark as done.
    """
    collection = get_collection()
    collection.update_one({"_id": ObjectId(todo_id)}, {"$set": {"status": "Done"}})
