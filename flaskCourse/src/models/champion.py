"""This is the module for handling champions on league of legends"""


class Champion:
    """This class represents a champion in league of legends"""

    def __init__(self, name: str, lane: str):
        self._name = name
        self._lane = lane
        self._level = 1

    def __str__(self):
        return f"The champion {self._name} is a {self._lane}"

    @property
    def name(self):
        """The champion name"""
        return self._name

    @property
    def lane(self):
        """The champion lane"""
        return self._lane
