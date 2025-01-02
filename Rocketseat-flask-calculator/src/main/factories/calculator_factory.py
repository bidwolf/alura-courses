"""
This module contains the factory responsible to instantiate the calculator
"""

from typing import Literal, Union
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_1 import FirstCalculator
from src.calculators.calculator_2 import SecondCalculator
from src.calculators.calculator_3 import ThirdCalculator
from src.calculators.interfaces.calculator_interface import CalculatorInterface


def calculator_1_factory():
    """This function creates an instance of the first calculator"""

    calculator = FirstCalculator()
    return calculator


def calculator_2_factory():
    """This function creates an instance of the second calculator"""
    calculator = SecondCalculator(NumpyHandler)
    return calculator


def calculator_3_factory():
    """This function creates an instance of the second calculator"""
    calculator = ThirdCalculator(NumpyHandler)
    return calculator


def calculator_factory(
    calculator_type: Union[Literal["first"], Literal["second"], Literal["third"]]
) -> CalculatorInterface:
    """
    This function creates an instance of a Calculator Interface based on the given calculator_type
    """
    match calculator_type:
        case "first":
            return calculator_1_factory()
        case "second":
            return calculator_2_factory()
        case "third":
            return calculator_3_factory()
