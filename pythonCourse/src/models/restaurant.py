"""
This model is responsible for the business logic of each restaurant
"""

from src.models.evaluation import Evaluation


class Restaurant:
    """Restaurant model"""

    def __init__(self, name: str, category: str):
        self._name = name
        self._category = category
        self._active = False
        self._evaluations = []

    def __str__(self):
        return (
            f"| {self._name.ljust(20)}"
            + f" | {self._category.ljust(20)} | "
            + f"{self.active.ljust(20)}"
            + " |"
            + f" {self.score_average:.2f}".ljust(20)
            + " |"
        )

    @property
    def name(self):
        """Manage the returned value for the name property"""
        return self._name

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

    def evaluate(self, client, score: int):
        """receive a evaluation from the client"""
        restaurant_evaluation = Evaluation(client=client, score=score)
        self._evaluations.append(restaurant_evaluation)

    @property
    def score_average(self) -> float:
        """return the score_average for the current restaurant"""
        if len(self._evaluations) == 0:
            return 0.0
        total = sum(evaluate.score for evaluate in self._evaluations)
        return float(total / len(self._evaluations))
