""" Module for restaurant menu class"""

from abc import ABC, abstractmethod


class RestaurantMenu(ABC):
    """This class represents a restaurant menu"""

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @abstractmethod
    def give_discount(self):
        """Abstract method for give a discount for a item in the menu
        - Must have a product_id or item_id to give the discount
        """

    @property
    def name(self):
        """returns the item name"""
        return self._name

    @property
    def price(self):
        """returns the item price"""
        return self._price
