""""""

from typing import Dict
from abc import ABC, abstractmethod
from flask import Request as FlaskRequest


class CalculatorInterface(ABC):
    """The calculator interface"""

    @abstractmethod
    def calculate(self, request: FlaskRequest) -> Dict:
        """Method responsible to handle the calculate logic"""
