"""
This model is responsible for the business logic of each restaurant
"""

from src.models.evaluation import Evaluation
from src.models.menu.restaurant_menu import RestaurantMenu
from src.models.menu.drink import Drink
from src.models.menu.food import Food


class Restaurant:
    """Restaurant model"""

    def __init__(self, name: str, category: str):
        self._name = name
        self._category = category
        self._active = False
        self._evaluations = []
        self._restaurant_menu = []

    def __str__(self):
        return (
            f"| {self._name.ljust(20)}"
            + f" | {self._category.ljust(20)} | "
            + f"{self.active.ljust(20)}"
            + " |"
            + f" {self.score_average}".ljust(20)
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
            return "-"
        total = sum(evaluate.score for evaluate in self._evaluations)
        return round(total / len(self._evaluations), 1)

    def show_menu(self):
        """print a menu of drinks"""
        print(f"{self._name} Menu:")
        for index, item in enumerate(self._restaurant_menu, start=1):
            if isinstance(item, Drink):
                print(f"{index} - {item.name} ({item.size} mL) R$ {item.price}")
                continue
            if isinstance(item, Food):
                print(f"{index} - {item.name} R$ {item.price}\n")
                print(f"Description: {item.description}")

    def create_option_menu(self, item_menu: RestaurantMenu):
        """create a menu option and append to the menu"""
        if not isinstance(item_menu, RestaurantMenu):
            print("We can't add this item to the menu.")
            return
        self._restaurant_menu.append(item_menu)
        if isinstance(item_menu, Food):
            print("The food was added to the menu.")
            return
        if isinstance(item_menu, Drink):
            print("The drink was added to the menu.")
