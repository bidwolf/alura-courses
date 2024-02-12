"""Module focused on python course of Alura"""

import os
from challenges.between_break_lines import between_break_lines


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


def invalid_option():
    """THis function re-run the app after the user type any key"""
    input("Type any key to come back to the menu:")
    main()


def run_option(selected_option: int, options: list):
    """Executes the selected option in the options available"""
    print(f"You select: {selected_option}\n")
    match selected_option:
        case 1:
            print(options[0])
        case 2:
            print(options[1])
        case 3:
            print(options[2])
        case 4:
            exit_app()
        case _:
            print(f"{selected_option} is not a valid option dude.\n")
            invalid_option()


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
        invalid_option()


if __name__ == "__main__":
    main()
