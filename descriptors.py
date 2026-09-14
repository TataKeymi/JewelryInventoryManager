from exceptions import InvalidPriceError


class PositivePrice:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, obj_type=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise InvalidPriceError("Price must be greater than 0.")
        setattr(obj, self.private_name, value)
