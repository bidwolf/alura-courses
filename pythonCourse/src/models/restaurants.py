"""
This model is responsible for the business logic of each restaurant
"""


class Restaurant:
    """Restaurant model"""

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
        self.active = False
