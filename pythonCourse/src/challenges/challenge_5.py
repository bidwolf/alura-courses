"""Module to contains the 5th challenge"""

from src.models.restaurants import Restaurant


def challenge_5():
    """The challenge 5 code"""
    italianiza_restaurant = Restaurant()
    italianiza_restaurant.name = "Italian Restaurant"
    italianiza_restaurant.category = "Italian"
    print(italianiza_restaurant.active)
    italianiza_restaurant.active = True
    print(italianiza_restaurant.active)
    pizza_restaurant = Restaurant()
    pizza_restaurant.name = "Pizza Place"
    pizza_restaurant.category = "Fast Food"
    print(f"the category of {pizza_restaurant.name} is {pizza_restaurant.category}")
    pizza_restaurant.active = True
