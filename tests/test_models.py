import json

import pytest

from exceptions import (InsufficientStockError,
                        InvalidSaleQuantityError,
                        InvalidPriceError)

from inventory import low_stock_items

from storage import save_inventory, load_inventory

from models import JewelryItem, Ring, Earrings


def test_sell_item():
    item = JewelryItem(name="test", material="test", price=100, quantity=5)
    result = item.sell(2)
    assert result == 200
    assert item.quantity == 3


def test_sell_more_than_in_stock():
    item = JewelryItem(name="test", material="test", price=100, quantity=5)
    with pytest.raises(InsufficientStockError):
        item.sell(6)


@pytest.mark.parametrize(
    "quantity_to_sell",
    [
        0,
        -1,
        -10
    ]
)
def test_sell_less_than_or_equal_to_zero(quantity_to_sell):
    item = JewelryItem(name="test", material="test", price=100, quantity=5)
    with pytest.raises(InvalidSaleQuantityError):
        item.sell(quantity_to_sell)


@pytest.mark.parametrize(
    "quantity_to_sell, expected_total, expected_quantity",
    [
        (1, 100, 4),
        (2, 200, 3),
        (3, 300, 2),
    ]
)
def test_sell_correct(quantity_to_sell, expected_total, expected_quantity):
    item = JewelryItem(name="test", material="test", price=100, quantity=5)
    result = item.sell(quantity_to_sell)
    assert item.quantity == expected_quantity
    assert result == expected_total


@pytest.mark.parametrize(
    "invalid_price",
    [
        0,
        -1,
        -100
    ]
)
def test_invalid_price(invalid_price):
    with pytest.raises(InvalidPriceError):
        JewelryItem(
            name="test",
            material="test",
            price=invalid_price,
            quantity=5
        )


def test_change_price():
    item = JewelryItem(
        name="test",
        material="test",
        price=100,
        quantity=5
    )
    item.price = 250
    assert item.price == 250


def test_slots_prevent_new_attributes():
    item = JewelryItem(
        name="test",
        material="test",
        price=100,
        quantity=5
    )
    with pytest.raises(AttributeError):
        item.random_attribute = 10


def test_ring_inherits_jewelry_item_attributes():
    ring = Ring(
        name="test",
        material="test",
        price=100,
        quantity=5,
        size=16.5
    )
    assert ring.price == 100
    assert ring.quantity == 5
    assert ring.size == 16.5


def test_discount_for_ring():
    ring = Ring(
        name="test",
        material="test",
        price=1000,
        quantity=5,
        size=16.5
    )
    ring.apply_discount(10)
    assert ring.price == 900


def test_low_stock_items():
    items = [
        JewelryItem(
            name="Jewelry",
            material="silver",
            price=10,
            quantity=5
        ),
        Ring(
            name="Ring",
            material="gold",
            price=200,
            quantity=2,
            size=18
        ),
        Earrings(
            name="Earrings",
            material="silver",
            price=10,
            quantity=1,
            fastening_type="stud"
        ),
    ]
    result = list(low_stock_items(items, 2))
    assert len(result) == 2
    assert all(item.quantity <= 2 for item in result)


def test_save_inventory(tmp_path):
    items = [
        JewelryItem(
            name="Jewelry",
            material="silver",
            price=10,
            quantity=5
        ),
        Ring(
            name="Ring",
            material="gold",
            price=200,
            quantity=5,
            size=18
        )
    ]
    expected_result = [
        {
            "name": "Jewelry",
            "material": "silver",
            "price": 10,
            "quantity": 5
        },
        {
            "name": "Ring",
            "material": "gold",
            "price": 200,
            "quantity": 5,
            "size": 18
        }
    ]
    file_path = tmp_path / "inventory.json"
    save_inventory(items, file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        loaded_items = json.load(file)
    assert loaded_items == expected_result


def test_load_inventory(tmp_path):
    file_path = tmp_path / "inventory.json"
    file_items = [
        {
            "name": "Jewelry",
            "material": "silver",
            "price": 10,
            "quantity": 5
        },
        {
            "name": "Ring",
            "material": "gold",
            "price": 200,
            "quantity": 5,
            "size": 18
        }
    ]
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(file_items, file, indent=4)
    loaded_items = load_inventory(file_path)
    assert len(loaded_items) == 2
    assert isinstance(loaded_items[0], JewelryItem)
    assert isinstance(loaded_items[1], Ring)
    assert loaded_items[0].name == "Jewelry"
    assert loaded_items[1].name == "Ring"
    assert loaded_items[0].material == "silver"
    assert loaded_items[1].material == "gold"
    assert loaded_items[0].price == 10
    assert loaded_items[1].price == 200
    assert loaded_items[0].quantity == 5
    assert loaded_items[1].quantity == 5
    assert loaded_items[1].size == 18
