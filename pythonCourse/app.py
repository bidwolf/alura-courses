"""Module focused on python course of Alura"""

import os
from src.challenges.between_break_lines import between_break_lines
from src.challenges.challenge_1 import challenge_1
from src.challenges.challenge_2 import challenge_2
from src.challenges.challenge_3 import challenge_3
from src.challenges.challenge_4 import challenge_4
from src.challenges.challenge_5 import challenge_5
from src.models.application import Application

RESTAURANTS = []
RESTAURANT_DICT = [
    {"name": "BK", "category": "hamburgers", "active": False},
    {"name": "MCDonald's", "category": "hamburgers", "active": False},
]
VERSIONS = [
    {
        "version": 1,
        "description": "Using only strings, lists to register a restaurant"
        + " and see all created restaurants",
    },
    {
        "version": 2,
        "description": "Using dictionaries to create and list restaurants"
        + "and turn it active/disable",
    },
    {"version": 3, "description": "Using classes and OOP to implements the logic"},
]


def print_line(character: str, repeat: int):
    """Print the {str} in {repeat} times"""
    print(f"{character*repeat}")


def show_version_menu():
    """Defines a menu that show all versions available"""
    print_line("*", 120)
    available_versions = []
    for version in VERSIONS:
        print(f"\n{version.get('version')} . {version.get('description')}")
        available_versions.append(version.get("version"))
    print("\n")
    print_line("*", 120)
    try:
        version = int(input("Please select a version:\n"))
    except ValueError as exception:
        if isinstance(exception, ValueError):
            print("Please insert a valid option.")
            show_version_menu()
    if version in available_versions:
        run_app(version=version)
    else:
        print("This version is not available!")
        show_version_menu()


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
    run_app(version=version)


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
            clear_prompt()
            print(f"Selected option: {options[3]}")
            show_version_menu()
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
    clear_prompt()
    try:
        print("Sabor Express\n")
        print(f"------------------ VERSION  {version} ------------------\n")
        options_available = get_options_available()
        show_options(options_available)
        selected_option = int(input("select one option:\n"))
        run_option(selected_option, options=options_available, version=version)
    except ValueError as exception:
        if isinstance(exception, ValueError):
            print("You must type a integer number dude.\n")
        rerun_app(version=version)


def get_options_available():
    """This function gets the available options based on the current version"""
    options_available = [
        "1. Register restaurant",
        "2. List restaurant",
        "3. Activate/disable restaurant",
        "4. Change version",
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
        case 5:
            print("\nchallenge five: dictionaries\n")
            challenge_5()
        case _:
            print("NOT NOT\n")


app = Application()


def main():
    """The main Function"""
    # clear_prompt()
    # # print("------------------ CHALLENGES ------------------\n")
    # for i in range(5, 6):
    #     run_challenge(number=i)
    # # show_version_menu()
    # burger_king_restaurant = Restaurant(name="Burger King", category="Hamburger")
    # print(vars(burger_king_restaurant))
    app.run()
    app.bump_version(bump_type="PATCH")
    print(app)


if __name__ == "__main__":
    main()
