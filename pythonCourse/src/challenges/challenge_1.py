""" Module for the first challenge about strings"""

from src.challenges.between_break_lines import between_break_lines


def challenge_1():
    """the first challenge"""
    print("Python on Alura Programming School \n")

    # Using loop
    between_break_lines("ALURA")

    # Using Sep
    print("A", "L", "U", "R", "A", sep="\n")

    pi = 3.14159

    # Using Round
    print(f"{round(pi, 2)}")
    # Using o método f-string
    print(f"{pi:.2f}")
    # Using f-string
    print(f"{pi:.2f}")

    name = "Henrique de Paula Rodrigues"
    age = 23
    print(name, age)
