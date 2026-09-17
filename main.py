from models import JewelryItem, Ring, Earrings

from storage import save_inventory


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


items_to_save = []

for item in items:
    item_data = {
        "name": item.name,
        "material": item.material,
        "price": item.price,
        "quantity": item.quantity
    }
    if isinstance(item, Ring):
        item_data["size"] = item.size
    if isinstance(item, Earrings):
        item_data["fastening_type"] = item.fastening_type
    items_to_save.append(item_data)


save_inventory(items_to_save, "inventory.json")
