"""Module focused on python course of Alura"""

import os
from challenges.between_break_lines import between_break_lines


def exit_app():
    """This function clear the prompt"""
    if os.name == "posix":
        os.system("clear")  # -> unix like Operation System
    else:
        os.system("cls")  # -> windows Operation System
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
        case _:
            exit_app()


def main():
    """The main Function"""
    print("Sabor Express\n")
    show_options(options_available)
    selected_option = int(input("select one option:"))
    run_option(selected_option, options=options_available)


if __name__ == "__main__":
    main()
