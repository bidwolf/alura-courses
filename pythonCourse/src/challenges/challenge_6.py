"""Module for the 6th challenge"""


# 1. Create a class named Car with model, color and year attributes
class Car:
    """Class that represents a car"""

    model = ""
    color = ""
    fabrication_year = int


class Client:
    """Class that represents a client"""

    _id = ""
    _name = ""
    _priority = "low"
    _account_benefits = None

    def __init__(self, client_id: str, name: str, priority: str):
        self._id = client_id
        self._name = name
        self._priority = priority

    def __str__(self):
        return f"client: {self._name}, has a {self._priority} in our customer service."


class AnotherRestaurant:
    """just another restaurant class for the challenge"""

    name = ""
    category = ""
    active = False
    popularity = ""
    foundation_year = 1900

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
        self.active = False
        self.popularity = "Low"

    def __str__(self):
        return (
            f"name:{self.name},"
            + f"popularity:{self.popularity},"
            + f"active:{self.active},"
            + f"category:{self.category},"
            + f"foundation_year:{self.foundation_year},"
        )


def challenge_6():
    """The challenge 6 code"""
    gol = Car()
    gol.model = "squared"
    gol.fabrication_year = 1999
    gol.color = "green"
    print(gol.model, gol.fabrication_year, gol.color)
    bk_restaurant = AnotherRestaurant(name="squared restaurant", category="Mexican")
    bk_restaurant.active = True
    bk_restaurant.popularity = "Big"
    bk_restaurant.foundation_year = 1980
    print(bk_restaurant)
    cliente_1 = Client(client_id=1, name="Joana", priority="low")
    cliente_2 = Client(client_id=2, name="Adriana", priority="low")
    cliente_3 = Client(client_id=3, name="Juliana", priority="low")
    cliente_4 = Client(client_id=4, name="Mariana", priority="low")
    print(f"{cliente_1}\n{cliente_2}\n{cliente_3}\n{cliente_4}")
