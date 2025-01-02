"""This module contain the driver handler interface for standard derivation calculators"""

from abc import ABC, abstractmethod
from typing import List


class DriverHandlerInterface(ABC):
    """This is an interface for a driver responsible to calculate a standard derivation"""

    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        """This method is responsible to calculate the standard derivation of a list of numbers"""

    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        """This method is responsible to calculate the variance of a list of numbers"""
