from exceptions import (InsufficientStockError,
                        InvalidSaleQuantityError)

from descriptors import PositivePrice


class JewelryItem:
    __slots__ = ("name", "material", "_price", "quantity")

    price = PositivePrice()

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


class DiscountMixin:
    def apply_discount(self, percent):
        self.price = self.price * (100 - percent) / 100


class Ring(DiscountMixin, JewelryItem):
    __slots__ = ("size",)

    def __init__(self, name, material, price, quantity, size):
        super().__init__(name, material, price, quantity)
        self.size = size

    def __str__(self):
        return super().__str__() + f" | {self.size}"


class Earrings(JewelryItem):
    __slots__ = ("fastening_type",)

    def __init__(self, name, material, price, quantity, fastening_type):
        super().__init__(name, material, price, quantity)
        self.fastening_type = fastening_type

    def __str__(self):
        return super().__str__() + f" | {self.fastening_type}"
