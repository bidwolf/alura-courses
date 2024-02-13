"""Module focused on python course of Alura"""

import os
from src.challenges.between_break_lines import between_break_lines
from src.challenges.challenge_1 import challenge_1
from src.challenges.challenge_2 import challenge_2
from src.challenges.challenge_3 import challenge_3
from src.challenges.challenge_4 import challenge_4

RESTAURANTS = []
RESTAURANT_DICT = [
    {"name": "BK", "category": "hamburgers", "active": False},
    {"name": "MCDonald's", "category": "hamburgers", "active": False},
]


def clear_prompt():
    """This function clear the prompt"""
    if os.name == "posix":
        os.system("clear")  # -> unix like Operation System
    else:
        os.system("cls")  # -> windows Operation System


def exit_app():
    """This function exit from the app"""
    clear_prompt()
    print("the app is ended\n")


# Actually we have a better way to do that


def show_options(options: list):
    """Show the options available in the program"""
    between_break_lines(word=options)


def rerun_app(version=1):
    """THis function re-run the app after the user type any key"""
    input("Type any key to come back to the menu:")
    main(version=version)


def run_option(selected_option: int, options: list, version=1):
    """Executes the selected option in the options available"""
    print(f"You select: {selected_option}\n")
    match selected_option:
        case 1:
            print(options[0])
            new_restaurant = input("Type the restaurant name:\n")
            if version == 1:
                register_new_restaurant(restaurant_name=new_restaurant)
            elif version == 2:
                restaurant_category = input("Type the restaurant category:\n")
                register_new_restaurant(
                    restaurant_name=new_restaurant,
                    restaurant_category=restaurant_category,
                    version=version,
                )
        case 2:
            print(options[1])
            if version == 1:
                list_restaurants()
            elif version == 2:
                list_restaurants_dict()
        case 3:
            print(options[2])
            if version == 2:
                restaurant_name = input(
                    "type the restaurant that you want to activate:\n"
                )
                activate_restaurant(restaurant_name=restaurant_name)
            elif version == 1:
                print(
                    "This app version don't have this feature, please, change to version 2"
                )
            rerun_app(version=version)
        case 4:
            print(options[3])
            if version == 1:
                main(version=2)
            elif version == 2:
                main(version=1)
        case 5:
            exit_app()
        case _:
            print(f"{selected_option} is not a valid option dude.\n")
            rerun_app(version=version)


def activate_restaurant(restaurant_name):
    """
    IMPORTANT: This function only works in version 2.
    This function is responsible to make a restaurant active
    """
    for restaurant in RESTAURANT_DICT:
        if restaurant_name in restaurant.values():
            restaurant["active"] = not restaurant["active"]
            print(
                f"Restaurant: {restaurant_name} now is ",
                "active" if restaurant["active"] is True else "disabled",
            )
            rerun_app(version=2)
            return
        print(f"Cannot find restaurant named {restaurant_name}")
        rerun_app(version=2)


def register_new_restaurant(
    restaurant_name: str,
    restaurant_category: str = None,
    version=1,
):
    """This function add a restaurant in the restaurant list
    1. has support to the first version
    2. support dictionaries
    """
    if version == 1:
        if restaurant_name not in RESTAURANTS:
            RESTAURANTS.append(restaurant_name)
        print("Restaurant added successfully!")
        rerun_app(version=1)
        return
    if version == 2:
        existent_restaurant = None
        for restaurant in RESTAURANT_DICT:
            if restaurant_name in restaurant.values():
                existent_restaurant = True
        if existent_restaurant is None:
            new_restaurant = {
                "name": restaurant_name,
                "category": (
                    restaurant_category if restaurant_category is not None else "empty"
                ),
                "active": False,
            }
            RESTAURANT_DICT.append(new_restaurant)
            print("Restaurant added successfully!")
            rerun_app(version=2)
        else:
            print("The restaurant already exists")
            rerun_app(version=2)


def list_restaurants():
    """List the Restaurant list"""
    print("|", "restaurant_id".ljust(20), "|", "restaurant_name".ljust(20), "|")
    for index, restaurant in enumerate(RESTAURANTS):
        line = "-" * (47)
        if index == 0:
            print(line)
        print(f"| {str(index).ljust(20)} | {restaurant.ljust(20)} |")
    rerun_app(version=1)


def list_restaurants_dict():
    """List the Restaurant dictionary list"""
    print(
        "\n| Restaurant_id\t| Restaurant_name |\t| Restaurant_category |\t| Active |\t"
    )
    for index, restaurant in enumerate(RESTAURANT_DICT):
        print(
            f"| {index}\t| {restaurant.get('name')}"
            + f" | {restaurant.get('category')}"
            + f" | {restaurant.get('active')} |\t"
        )
    rerun_app(version=2)


def run_app(version=1):
    """This function runs the main app"""
    try:
        print("Sabor Express\n")
        print(f"------------------ VERSION  {version} ------------------\n")
        options_available = get_options_available(version=version)
        show_options(options_available)
        selected_option = int(input("select one option:\n"))
        run_option(selected_option, options=options_available, version=version)
    except ValueError as exception:
        if isinstance(exception, ValueError):
            print("You must type a integer number dude.\n")
        rerun_app(version=version)


def get_options_available(version=1):
    """This function gets the available options based on the current version"""
    options_available = [
        "1. Register restaurant",
        "2. List restaurant",
        "3. Activate/disable restaurant",
        "4. Change to version 2" if version == 1 else "4. Change to version 1",
        "5. exit",
    ]
    return options_available


def run_challenge(number: int):
    """Run the challenge"""
    match number:
        case 1:
            print("challenge one: strings\n")
            challenge_1()
        case 2:
            print("\nchallenge two: exceptions and if/else statement\n")
            challenge_2()
        case 3:
            print("\nchallenge three: lists and for loop\n")
            challenge_3()
        case 4:
            print("\nchallenge four: dictionaries\n")
            challenge_4()
        case _:
            print("NOT NOT\n")


def main(version=1):
    """The main Function"""
    clear_prompt()
    run_app(version=version)
    print("------------------ CHALLENGES ------------------\n")
    for i in range(5):
        run_challenge(number=i)


if __name__ == "__main__":
    main()
