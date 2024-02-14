"""
This model is responsible for the business logic of each restaurant
"""


class Restaurant:
    """Restaurant model"""

    def __init__(self, name: str, category: str):
        self._name = name
        self._category = category
        self._active = False

    def __str__(self):
        return (
            f"| {self._name.ljust(20)}"
            + f" | {self._category.ljust(20)} | "
            + f"{self.active.ljust(20)}"
            + " |\t"
        )

    @property
    def name(self):
        """Manage the returned value for the name property"""
        return self._name.capitalize()

    @property
    def active(self):
        """Manage the returned value for the active property"""
        return "✅" if self._active is True else "❎"

    def activate(self):
        """This method activates the restaurant"""
        self._active = True

    def disable(self):
        """This method disable the restaurant"""
        self._active = False
