from exceptions import InsufficientStockError, InvalidSaleQuantityError


class JewelryItem:
    def __init__(self, name, material, price, quantity):
        self.name = name
        self.material = material
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"{self.name} | {self.material} | {self.price} UAH |"
                f" {self.quantity} {'pc' if self.quantity == 1 else 'pcs'}")

    def sell(self, quantity_to_sell):
        if quantity_to_sell > self.quantity:
            raise InsufficientStockError(
                "Quantity to sell cannot be greater than quantity in stock"
            )
        if quantity_to_sell <= 0:
            raise InvalidSaleQuantityError(
                "Quantity to sell cannot be less than or equal to 0"
            )
        self.quantity -= quantity_to_sell
        return quantity_to_sell * self.price
