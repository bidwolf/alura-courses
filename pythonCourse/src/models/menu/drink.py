""" Module for drink menu of a restaurant class"""

from src.models.menu.restaurant_menu import RestaurantMenu


class Drink(RestaurantMenu):
    """This class represents a restaurant drink menu item"""

    def __init__(self, name, price, size):
        super().__init__(name=name, price=price)
        self._size = size

    def __str__(self):
        return f"{self._name},{self._price},{self._size}"
