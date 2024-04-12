import os
import requests
import pytest
from dotenv import load_dotenv, find_dotenv

from todo_app import app


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


class StubResponse:
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


def stub(_, url, params={}):
    test_board_id = os.getenv("BOARD_ID")
    test_key = os.getenv("TRELLO_API_KEY")
    test_token = os.getenv("TRELLO_API_TOKEN")
    if (
        url
        == f"https://api.trello.com/1/boards/{test_board_id}/cards?key={test_key}&token={test_token}"
    ):
        fake_response_data = [
            {
                "id": "123abc",
                "idList": os.getenv("NOT_STARTED_LIST_ID"),
                "name": "Test card",
            }
        ]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')


def test_index_page(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, "request", stub)

    # Make a request to our app's index page
    response = client.get("/")

    assert response.status_code == 200
    assert "Test card" in response.data.decode()
