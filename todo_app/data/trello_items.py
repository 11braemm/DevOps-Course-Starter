import requests
import os

from todo_app.data.Item import Item

def add_item(title):
    print(title)
    """
    Adds a new item with the specified title to Trello.

    Args:
        title: The title of the item.
    """
    reqUrl = (
        f"https://api.trello.com/1/cards?"
        f"idList={os.getenv('NOT_STARTED_LIST_ID')}&"
        f"key={os.getenv('TRELLO_API_KEY')}&"
        f"token={os.getenv('TRELLO_API_TOKEN')}&"
        f"name={title}"
    )

    requests.request("POST", reqUrl)

def get_items():
    """
    Fetches all saved items from Trello.

    Returns:
        list: The list of saved items.
    """
    reqUrl = (
        f"https://api.trello.com/1/boards/"
        f"{os.getenv('BOARD_ID')}/cards?"
        f"key={os.getenv('TRELLO_API_KEY')}&"
        f"token={os.getenv('TRELLO_API_TOKEN')}"
    )

    response = requests.request("GET", reqUrl)

    return [ Item.from_trello_card(item) for item in response.json()]
    
def mark_item_as_done(card_id):
    """
    Marks the Trello card with the specified ID as done by moving it to the "Done" list.

    Args:
        card_id: The ID of the Trello card to mark as done.
    """
    reqUrl = (
        f"https://api.trello.com/1/cards/{card_id}?"
        f"idList={os.getenv('DONE_LIST_ID')}&"  # Change to your "Done" list ID
        f"key={os.getenv('TRELLO_API_KEY')}&"
        f"token={os.getenv('TRELLO_API_TOKEN')}"
    )

    requests.request("PUT", reqUrl)
