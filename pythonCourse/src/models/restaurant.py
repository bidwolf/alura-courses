"""
This model is responsible for the business logic of each restaurant
"""


class Restaurant:
    """Restaurant model"""

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
        self.active = False

    def __str__(self):
        return (
            f"| {self.name.ljust(20)}"
            + f" | {self.category.ljust(20)} | "
            + ("Active".ljust(20) if self.active is True else "Disabled".ljust(20))
            + " |\t"
        )

    def activate(self):
        """This method activates the restaurant"""
        self.active = True

    def disable(self):
        """This method disable the restaurant"""
        self.active = False
