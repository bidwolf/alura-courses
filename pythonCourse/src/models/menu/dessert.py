"""Module that contains the dessert class"""

from src.models.menu.restaurant_menu import RestaurantMenu


class Dessert(RestaurantMenu):
    """That class represents a dessert item for a restaurant menu"""

    def __init__(self, name, price, weight):
        super().__init__(name=name, price=price)
        self._weight = weight

    def give_discount(self):
        return self._price * 0.99

    @property
    def weight(self):
        """this method returns the dessert weight in grams"""
        return self._weight
