import os


class Item:
    def __init__(self, id, name, status="Not started"):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_mongo_document(cls, document):
        return Item(
            document["_id"],
            document["description"],
            document["status"]
        )
