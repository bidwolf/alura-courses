"""Module focused on python course of Alura"""

from src.models.application import Application
from src.models.menu.drink import Drink
from src.models.menu.food import Food


app = Application()


def main():
    """The main Function"""
    # clear_prompt() # version sequential
    # show_version_menu() # version sequential
    # app.run()
    # print("------------------ CHALLENGES ------------------\n")
    # for i in range(8, 9):
    #     run_challenge(number=i)
    # app.bump_version(bump_type="PATCH")
    # print(app)
    bred = Food(description="sugar bred", name="Bred", price=20.00)
    lemonade = Drink(name="Bred", price=20.00, size="large")
    print(bred)
    print(lemonade)


if __name__ == "__main__":
    main()
