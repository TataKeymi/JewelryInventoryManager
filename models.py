from exceptions import (InsufficientStockError,
                        InvalidSaleQuantityError,
                        InvalidDiscountError)

from descriptors import PositivePrice

from decorators import log_action


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

    def __repr__(self):
        return self.__str__()

    @log_action("SALE")
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

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "material": self.material,
            "price": self.price,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class DiscountMixin:
    __slots__ = ()

    @staticmethod
    def validate_discount(percent):
        return 0 < percent < 100

    def apply_discount(self, percent):
        if not self.validate_discount(percent):
            raise InvalidDiscountError("Discount percentage must be between 0 and 100.")
        self.price = self.price * (100 - percent) / 100


class Ring(DiscountMixin, JewelryItem):
    __slots__ = ("size",)

    def __init__(self, name, material, price, quantity, size):
        super().__init__(name, material, price, quantity)
        self.size = size

    def __str__(self):
        return super().__str__() + f" | {self.size}"

    def to_dict(self):
        data = super().to_dict()
        data["size"] = self.size
        return data


class Earrings(JewelryItem):
    __slots__ = ("fastening_type",)

    def __init__(self, name, material, price, quantity, fastening_type):
        super().__init__(name, material, price, quantity)
        self.fastening_type = fastening_type

    def __str__(self):
        return super().__str__() + f" | {self.fastening_type}"

    def to_dict(self):
        data = super().to_dict()
        data["fastening_type"] = self.fastening_type
        return data


data = {
    "name": "Jewelry",
    "material": "silver",
    "price": 100,
    "quantity": 5,
}

item = JewelryItem.from_dict(data)
item2 = JewelryItem("jewelry", "gold", 100, 10)

print(type(item))
# JewelryItem
print(type(item2))
