""" Challenge 2 - odd or even number with if else statement"""

import re


def odd_or_even(number: int) -> "even" or "odd":
    """This function tells if a number is odd or even"""
    if number % 2 == 0:
        return "even"
    return "odd"


def categorize_by_age(age: int) -> "adult" or "adolescent" or "child":
    """This function categorize the age as 'adult','adolescent' or 'child'"""
    if 0 <= age <= 12:
        return "child"
    if 12 < age < 18:
        return "adolescent"
    return "adult"


def verify_password(password: str) -> str:
    """
    This function verify if a password contains the min length and has almost:
    1 Uppercase letter, 1 lowercase letter, 1 number and 1 special character
    """
    password_regex = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W)")
    min_length = 13
    if len(password) >= min_length:
        if password_regex.search(password):
            return "Your password is strong."
        return (
            "Your password must almost have 1 uppercase letter,"
            + "1 lowercase letter, 1 special character and 1 number"
        )
    return "Your password must have almost 13 characters"


def verify_name(name: str) -> str:
    """This function verify if the name contains almost 3 characters."""
    if len(name) >= 3:
        return "Your name is nice"
    return "Your name must contain almost 3 characters"


def verify_origin_quadrant(x: float, y: float):
    """Verify the current quadrant of a point that have one or more points in the origin"""
    if x == 0 and y == 0:
        return "The point is in the origin"
    if x == 0:
        if y > 0:
            return "The point is in the first and second quadrant"
        return "The point is in the third and fourth quadrant"
    if y == 0:
        if x > 0:
            return "The point is in the first and fourth quadrant"
        return "The point is in the second and third quadrant"
    return "invalid point"


def verify_quadrant(x: float, y: float) -> str:
    """Verify the current quadrant of a point"""
    if x == 0 or y == 0:
        return verify_origin_quadrant(x, y)
    if x > 0:
        if y > 0:
            return "The point is in the first quadrant"
        return "The point is in the fourth quadrant"
    if y > 0:
        return "the point is in the second quadrant"
    return "the point is in the third quadrant"


# 1. tell if a number is odd or even
asked_number = int(input("Please type a number:\n"))
RESULT_1 = odd_or_even(number=asked_number)
print(f"The number is {RESULT_1}.")
# 2. Tell if the asked age is of a child, adolescent, or an adult
asked_age = int(input("Please tell me your age:\n"))
RESULT_2 = categorize_by_age(age=asked_age)
print(f"The age is of a {RESULT_2}.")
# 3. Tell if the name and password match the requirements
asked_name = input("Please insert your name:\n")
asked_password = input("Please insert a password:\n")
RESULT_3 = verify_password(password=asked_password)
RESULT_4 = verify_name(name=asked_name)
print(f"{RESULT_4}, and {RESULT_3}")
# 4. Tell what quadrant a point pertences
coordinate_x = float(input("Please insert the x coordinate:\n"))
coordinate_y = float(input("Please insert the y coordinate:\n"))
RESULT_5 = verify_quadrant(x=coordinate_x, y=coordinate_y)
print(f"{RESULT_5}")
