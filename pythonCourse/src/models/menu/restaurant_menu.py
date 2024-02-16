""" Module for restaurant menu class"""


class RestaurantMenu:
    """This class represents a restaurant menu"""

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
