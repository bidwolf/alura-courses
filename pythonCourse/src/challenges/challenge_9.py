"""This module represents the 9th challenge from the Alura course"""


class Vehicle:
    """This class represents a vehicle"""

    def __init__(self, model, fabricant):
        self._model = model
        self._fabricant = fabricant
        self._started = False

    def __str__(self):
        return (
            f"This {self._model} was manufactured by {self._fabricant } and it is turned"
            + ("on." if self._started else "off.")
        )


class Car(Vehicle):
    """This class represents a car"""

    def __init__(self, model, fabricant, doors):
        self._doors = doors
        super().__init__(model=model, fabricant=fabricant)

    def __str__(self):
        return super().__str__() + f" and has {self._doors} doors."


class Bike(Vehicle):
    """This class represents a Bike"""

    def __init__(self, model, fabricant, cylinder_capacity):
        self._cylinder_capacity = cylinder_capacity
        super().__init__(model=model, fabricant=fabricant)

    def __str__(self):
        return (
            super().__str__() + f" and has {self._cylinder_capacity} cylinder_capacity."
        )


def challenge_9():
    """This function runs all requirements of the 9th challenge from Alura"""
    focus = Car(doors=2, fabricant="Volkswagen", model="Focus sport")
    shineray = Bike(cylinder_capacity=3, fabricant="Honda", model="Shineray")
    print(focus)
    print(shineray)
