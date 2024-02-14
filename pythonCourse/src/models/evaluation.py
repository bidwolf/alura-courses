"""This module is responsible to provide a evaluation for a restaurant"""


class Evaluation:
    """This class handle the business logic about restaurant evaluation"""

    def __init__(self, client, score: int):
        assert 0 <= score <= 5, "You must type a value between 0 and 5"
        self._client = client
        self._score = score

    @property
    def score(self):
        """get the score of a evaluation"""
        return self._score
