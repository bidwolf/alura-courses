"""Module to contains the 5th challenge"""

from src.models.restaurant import Restaurant


def challenge_5():
    """The challenge 5 code"""
    italianiza_restaurant = Restaurant(name="Italian Restaurant", category="Italian")
    print(italianiza_restaurant.active)
    italianiza_restaurant.activate()
    print(italianiza_restaurant.active)
    pizza_restaurant = Restaurant(name="Pizza Place", category="Fast Food")
    print(pizza_restaurant)
    pizza_restaurant.activate()
