"""Module containing the fourth calculator logic"""

from typing import Dict, List
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .interfaces.calculator_interface import CalculatorInterface


class FourthCalculator(CalculatorInterface):
    """
    This class is responsible to solve the extra challenge from course
    - Should calculate return the average of a list
    """

    def __init__(self, driver: DriverHandlerInterface):
        self.__driver = driver()

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_data(body=body)
        self.__validate_list(numbers=input_data)
        result = self.__process_data(numbers=input_data)
        response = self.__format_response(result=result)
        return response

    def __validate_data(self, body: Dict) -> List[float]:
        """Method responsible to validate the request body"""
        if not body or not "numbers" in body:
            raise HttpBadRequestError(
                "The request body should have a field called numbers"
            )
        if not isinstance(body["numbers"], list):
            raise HttpBadRequestError("The numbers field should be a list of numbers")
        if len(body["numbers"]) == 0:
            raise HttpBadRequestError(
                "The numbers field should have at least one number"
            )
        return body["numbers"]

    def __validate_list(self, numbers: List[float]) -> None:
        """Method responsible to validate the numbers list to avoid operations in invalid data"""
        for n in numbers:
            if not isinstance(n, (int, float)):
                raise HttpUnprocessableEntityError(
                    "Calculator can't make operations in non numeric arguments"
                )

    def __process_data(self, numbers: List[float]) -> float:
        """Method responsible to calculate and return the average of the list"""
        average = self.__driver.average(numbers=numbers)
        return average

    def __format_response(self, result: float) -> Dict:
        """Method responsible to format the response for the response payload"""
        return {"data": {"calculator": 4, "result": round(result, 2)}}
