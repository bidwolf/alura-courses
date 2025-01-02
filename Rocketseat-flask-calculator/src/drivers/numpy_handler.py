"""This module is responsible to a Facade for the numpy library"""

from typing import List
import numpy
from .interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    """This is the numpy Facade Class"""

    def __init__(self):
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        result = self.__np.std(numbers)
        return result

    def variance(self, numbers):
        return self.__np.var(numbers)

    def average(self, numbers):
        return self.__np.average(numbers)
