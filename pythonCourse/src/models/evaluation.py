"""This module is responsible to provide a evaluation for a restaurant"""


class Evaluation:
    """This class handle the business logic about restaurant evaluation"""

    def __init__(self, client, score: int):
        self._client = (client,)
        self._score = score

    @property
    def score(self):
        """get the score of a evaluation"""
        return self._score
