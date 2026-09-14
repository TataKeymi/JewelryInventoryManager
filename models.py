class JewelryItem:
    def __init__(self, name, material, price, quantity):
        self.name = name
        self.material = material
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"{self.name} | {self.material} | {self.price} UAH |"
                f" {self.quantity} {'pc' if self.quantity == 1 else 'pcs'}")
