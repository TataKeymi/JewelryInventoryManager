class InsufficientStockError(Exception):
    """Raised when quantity to sell is greater than quantity in stock."""


class InvalidSaleQuantityError(Exception):
    """Raised when quantity to sell is less than or equal to 0."""


class InvalidPriceError(Exception):
    """Raised when price is less than or equal to 0."""


class UnknownJewelryTypeError(Exception):
    """Raised when an unknown jewelry type is requested."""


class InvalidDiscountError(Exception):
    """Raised when discount is less than or equal to 0 or greater than or equal to 100."""
