from models import JewelryItem, Ring, Earrings

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
    ),
    Earrings(
        name="Earrings",
        material="silver",
        price=10,
        quantity=5,
        fastening_type="stud"
    ),
]


def show_inventory(items):
    for item in items:
        print(item)


show_inventory(items)
