from models import (JewelryItem,
                    Ring,
                    Earrings)


def low_stock_items(items, limit):
    for item in items:
        if item.quantity <= limit:
            yield item


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
        quantity=0,
        fastening_type="stud"
    ),
]

print(list(low_stock_items(items, 2)))
