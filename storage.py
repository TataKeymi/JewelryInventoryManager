import json


def save_inventory(items, filename):
    with open(filename, "w") as file:
        json.dump(items, file, indent=4)
