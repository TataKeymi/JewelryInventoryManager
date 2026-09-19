import json

from models import JewelryItem, Ring, Earrings


def save_inventory(items, filename):
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
        elif isinstance(item, Earrings):
            item_data["fastening_type"] = item.fastening_type
        items_to_save.append(item_data)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(items_to_save, file, indent=4)


def load_inventory(filename):
    with open(filename, "r", encoding="utf-8") as file:
        items = json.load(file)
        loaded_items = []
        for item in items:
            if "size" in item:
                loaded_items.append(Ring(**item))
            elif "fastening_type" in item:
                loaded_items.append(Earrings(**item))
            else:
                loaded_items.append(JewelryItem(**item))
        return loaded_items
