"""Module focused on python course of Alura"""

import os
from src.challenges.between_break_lines import between_break_lines
from src.challenges.challenge_1 import challenge_1
from src.challenges.challenge_2 import challenge_2
from src.challenges.challenge_3 import challenge_3

RESTAURANTS = []


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


options_available = [
    "1. Register restaurant",
    "2. List restaurant",
    "3. Activate restaurant",
    "4. exit",
]
# Actually we have a better way to do that


def show_options(options: list):
    """Show the options available in the program"""
    between_break_lines(word=options)


def rerun_app():
    """THis function re-run the app after the user type any key"""
    input("Type any key to come back to the menu:")
    main()


def run_option(selected_option: int, options: list):
    """Executes the selected option in the options available"""
    print(f"You select: {selected_option}\n")
    match selected_option:
        case 1:
            print(options[0])
            new_restaurant = input("Type the restaurant name:\n")
            register_new_restaurant(restaurant_name=new_restaurant)
        case 2:
            print(options[1])
            list_restaurants()
        case 3:
            print(options[2])
        case 4:
            exit_app()
        case _:
            print(f"{selected_option} is not a valid option dude.\n")
            rerun_app()


def register_new_restaurant(restaurant_name: str):
    """This function add a restaurant in the restaurant list"""
    if restaurant_name not in RESTAURANTS:
        RESTAURANTS.append(restaurant_name)
    print("Restaurant added successfully!")
    rerun_app()


def list_restaurants():
    """List the Restaurant list"""
    print("\n| Restaurant_id\t| Restaurant_name |\t")
    for index, restaurant in enumerate(RESTAURANTS):
        print(f"| {index}\t| {restaurant} |\t")
    rerun_app()


def main():
    """The main Function"""
    clear_prompt()
    print("Sabor Express\n")
    show_options(options_available)
    try:
        selected_option = int(input("select one option:\n"))
        run_option(selected_option, options=options_available)
    except ValueError as exception:
        if isinstance(exception, ValueError):
            print("You must type a integer number dude.\n")
        rerun_app()
    print("------------------CHALLENGES------------------\n")
    print("challenge one: strings\n")
    challenge_1()
    print("\nchallenge two: exceptions and if/else statement\n")
    challenge_2()
    print("\nchallenge three: lists and for loop\n")
    challenge_3()


if __name__ == "__main__":
    main()
