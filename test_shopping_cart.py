from unittest.mock import Mock

import pytest

from item_database import ItemDatabase
from shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    cart = ShoppingCart(5)

    for _ in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")


def test_can_get_total_price(cart):
    cart = ShoppingCart(5)

    cart.add("apple m1")
    cart.add("apple m2")
    cart.add("apple m3")

    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    price_map = {
        "apple m1": 1.0,
        "apple m2": 2.0,
        "apple m3": 3.0
    }

    item_database.get = Mock(return_value=mock_get_item)
    assert cart.get_total_price(price_map) == 6.0
