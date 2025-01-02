"""The module to deal with the second calculator challenge"""

from typing import List, Dict
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from .interfaces.calculator_interface import CalculatorInterface


class SecondCalculator(CalculatorInterface):
    """
    This class is responsible to make calculations to solve the second calculation challenge

    ## Problem 02 - Second Calculator
    - N numbers are sent.
    - All these N numbers are multiplied by 11 and raised to the power of 0.95.
    - Finally, the standard deviation of these results is removed and the inverse of this value is returned (1/result)
    """

    def __init__(self, driver: DriverHandlerInterface) -> None:
        self.driver = driver()

    def calculate(self, request: FlaskRequest) -> Dict:
        """This method handles the second calculator logic"""
        body = request.json
        numbers = self.__validate_data(body=body)
        result = self.__process_data(numbers=numbers)
        response = self.__format_response(result=result)
        return response

    def __first_step_map_handler(self, number: float) -> float:
        if not isinstance(number, (float, int)):
            raise ValueError("The numbers field should be a list of numbers")

        return (number * 11) ** 0.95

    def __format_response(self, result: float) -> Dict:
        return {"data": {"calculator": 2, "result": round(result, 2)}}

    def __process_data(self, numbers: List[float]) -> float:
        """This method make multiplies each number by 11 and raise then to the power of 0.95."""
        transformed_numbers = [self.__first_step_map_handler(number=n) for n in numbers]
        std = self.driver.standard_derivation(numbers=transformed_numbers)
        result = 1 / std
        return result

    def __validate_data(self, body: Dict) -> List[float]:
        """This method is responsible to validate the request body"""
        if not body or not "numbers" in body:
            raise ValueError("The request body should have a field called numbers")
        if not isinstance(body["numbers"], list):
            raise ValueError("The numbers field should be a list of numbers")
        return body["numbers"]
