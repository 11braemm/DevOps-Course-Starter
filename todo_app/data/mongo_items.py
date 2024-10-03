import dotenv
import os
from bson import ObjectId
import pymongo

from todo_app.data.Item import Item

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))
db = client[os.getenv("MONGODB_DATABASE_NAME")]
collection = db[os.getenv("MONGODB_COLLECTION_NAME")]

def add_item(title: str):
    """
    Adds a new item with the specified title to MongoDB.

    Args:
        title: The title of the item.
    """
    new_to_do = {"status": "Not started", "description": title}
    collection.insert_one(new_to_do)


def get_items():
    """
    Fetches all saved items from MongoDB.

    Returns:
        list: The list of saved items.
    """
    mongo_documents = list(collection.find())
    items = [Item.from_mongo_document(document) for document in mongo_documents]
    # print(mongo_documents)
    # print(items[0].name, items[0].status)
    return [Item.from_mongo_document(document) for document in mongo_documents]


def mark_item_as_done(todo_id):
    """
    Marks the MongoDB with the specified ID as done.

    Args:
        card_id: The ID of the MongoDB item to mark as done.
    """
    collection.update_one({"_id": ObjectId(todo_id)}, {"$set": {"status": "Done"}})
