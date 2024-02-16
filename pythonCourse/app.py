"""Module focused on python course of Alura"""

from src.models.application import Application
from src.models.menu.drink import Drink
from src.models.menu.food import Food
from src.challenges.main import run_challenges
from src import app_sequential_version

app = Application()


def main():
    """The main Function"""
    app.run()
    app.bump_version(bump_type="PATCH")
    print(app)
    app_sequential_version.main()
    run_challenges()
    bred = Food(description="sugar bred", name="Bred", price=20.00)
    lemonade = Drink(name="Bred", price=20.00, size="large")
    print(bred)
    print(lemonade)


if __name__ == "__main__":
    main()
