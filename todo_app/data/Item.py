import os


class Item:
    def __init__(self, id, name, status = 'Not Started'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], 'Not started' if card['idList'] == os.getenv('NOT_STARTED_LIST_ID') else 'Done')
    