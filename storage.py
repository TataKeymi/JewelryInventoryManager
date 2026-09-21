import json

from models import JewelryItem, Ring, Earrings


def save_inventory(items, filename):
    items_to_save = [item.to_dict() for item in items]
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
