class InsufficientStockError(Exception):
    """Raised when quantity to sell is greater than quantity in stock."""


class InvalidSaleQuantityError(Exception):
    """Raised when quantity to sell is less than or equal to 0."""


class InvalidPriceError(Exception):
    """Raised when price is less than or equal to 0."""


class UnknownJewelryTypeError(Exception):
    """Raised when an unknown jewelry type is requested."""
