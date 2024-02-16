""" Module for restaurant a food menu class"""

from src.models.menu.restaurant_menu import RestaurantMenu


class Food(RestaurantMenu):
    """This class represents a restaurant food menu"""

    def __init__(self, name, price, description):
        super().__init__(name=name, price=price)
        self._description = description

    def __str__(self):
        return f"{self._name},{self._price},{self._description}"
