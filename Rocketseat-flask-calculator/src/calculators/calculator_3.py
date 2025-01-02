"""The module to deal with the third calculator challenge"""

from typing import Dict, List
from flask import Request as FlaskRequest
from src.calculators.interfaces.calculator_interface import CalculatorInterface
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class ThirdCalculator(CalculatorInterface):
    """
    - N numbers are entered as input
    - If the variance of all these numbers is less than their multiplication, success information is presented to the user.
    - Otherwise, failure information is presented.
    """

    def __init__(self, driver: DriverHandlerInterface):
        self.__driver = driver()

    def calculate(self, request: FlaskRequest):
        body = request.json
        data = self.__validate_data(body=body)
        result = self.__process_data(numbers=data)
        return self.__format_response(result=result)

    def __multiplication(self, numbers: List[float]) -> float:
        result = 1
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise HttpUnprocessableEntityError(
                    "Calculator can't make operations in non numeric arguments"
                )
            result *= number
        return result

    def __process_data(self, numbers: List[float]) -> float:
        """This method calculates and send the multi"""
        multiplication = self.__multiplication(numbers=numbers)
        variance = self.__driver.standard_derivation(numbers=numbers)
        self.__verify_results(variance, multiplication)
        return variance

    def __validate_data(self, body: Dict) -> List[float]:
        """This method is responsible to validate the request body"""
        if not body or not "numbers" in body:
            raise HttpBadRequestError(
                "The request body should have a field called numbers"
            )
        if not isinstance(body["numbers"], list):
            raise HttpBadRequestError("The numbers field should be a list of numbers")
        return body["numbers"]

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpUnprocessableEntityError(
                "The variance is less than the multiplication of each element on the list"
            )

    def __format_response(self, result: float) -> Dict:
        return {"data": {"calculator": 3, "result": round(result, 2)}}
