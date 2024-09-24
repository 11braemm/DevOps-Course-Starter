import pytest

from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item

not_started_item_1 = Item(1, "to do 1", "Not started")
not_started_item_2 = Item(2, "to do 2", "Not started")
done_item = Item(3, "to do 3", "Done")


@pytest.fixture
def test_items():
    return [not_started_item_1, done_item, not_started_item_2]


def test_view_model_correctly_filters_to_items_with_not_started_status(test_items):
    # Arrange
    view_model = ViewModel(test_items)

    # Act
    not_started_items_result = view_model.not_started_items

    # Assert
    assert len(not_started_items_result) == 2
    assert not_started_item_1 in not_started_items_result
    assert not_started_item_2 in not_started_items_result


def test_view_model_correctly_filters_to_items_with_done_status(test_items):
    # Arrange
    view_model = ViewModel(test_items)

    # Act
    done_items = view_model.done_items

    # Assert
    assert len(done_items) == 1
    assert done_item in done_items
