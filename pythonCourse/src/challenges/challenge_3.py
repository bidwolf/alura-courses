"""The third challenge module about lists and for loop"""

from src.challenges.challenge_2 import odd_or_even


def odd_sum(numbers: list) -> int:
    """return the sum of all odd numbers"""
    result = 0
    for num in numbers:
        if odd_or_even(num) == "odd":
            result += num
    return result


def better_odd_sum(numbers: list) -> int:
    """use my math knowledge to calculate the odd_sum"""
    # Since the are sequential starting from 0
    # (which means that we do not have a forgotten number in the sequence)
    last_number = numbers.pop()
    if odd_or_even(last_number) == "odd":
        return int((last_number + 1) / 2) ** 2
    return int(last_number / 2) ** 2


def load_names(quantity: int) -> list:
    """read a quantity of names and return a list of names"""
    names = []
    for i in range(0, quantity):
        name = input(f"Insert the {i+1}st name:\n")
        names.append(name)
    return names


def create_month_year_list():
    """create a list with the month and year typed from the user"""
    month_year_list = []
    try:
        month = int(input("type your birth month:\n"))
        if month <= 0 or month > 12:
            raise ValueError("Invalid month")
        year = int(input("type your birth year:\n"))
        month_year_list.append(month)
        month_year_list.append(year)
    except ValueError as exception:
        if exception == "Invalid month":
            print(exception)
        else:
            print("You must type integer numbers")
        return create_month_year_list()
    return month_year_list


def arithmetic_table(num: int):
    """prints the arithmetic table of num"""
    for i in range(11):
        print(f"{num} x {i} = {num*i}")


def summation(numbers: list):
    """Do a summation of a numbers list"""
    acc = 0
    for i in numbers:
        try:
            acc += float(i)
        except ValueError as exception:
            if isinstance(exception, ValueError):
                print("not convertible to number element was find, skipping...\n")
    return acc


def average(numbers: list):
    """calculates the average in a list"""
    total = summation(numbers=numbers)
    try:
        return total / len(numbers)
    except ZeroDivisionError as exception:
        if isinstance(exception, ZeroDivisionError):
            print("the list is empty")
    return 0


def challenge_3():
    """The third challenge"""

    names = load_names(4)
    numbers = []
    month_year_list = create_month_year_list()
    for num in range(1, 11):
        numbers.append(num)
    print(numbers)
    print(month_year_list)
    for name in names:
        print(name)
    print(odd_sum(numbers=numbers))
    print(better_odd_sum(numbers=numbers))  # This do not use loop
    for num in range(1, 11):
        print(11 - num)
    try:
        table_num = int(
            input("type a integer number to see the arithmetic table of that number:\n")
        )
        arithmetic_table(table_num)
    except ValueError as exception:
        if isinstance(exception, ValueError):
            print("An error ocurred, please in the next time insert a integer number")
    summation(["123", 123, 12.9, "asda"])
    summation([1, 2, 3, 4])
    print(f"the average of {[]} is: {average([])}")
    print(f"the average of {[1,2,3,4]} is: {average([1, 2, 3, 4])}")
