"""The module to deal with the first calculator challenge"""

from typing import Dict
from flask import Request as FlaskRequest
from .interfaces.calculator_interface import CalculatorInterface


class FirstCalculator(CalculatorInterface):
    """This class is responsible to make calculations to solve the first challenge
    A number is divided into 3 equal parts.
    - The first part is divided by 4 and its result is added to 7. After that, the result is squared and multiplied by a value of 0.257.
    - The second part is raised to the power of 2.121, divided by 5, and added to 1
    - The third part remains at the same value.
    - Finally, these 3 values are added and the result is given
    """

    def __init__(self) -> None:
        pass

    def calculate(self, request: FlaskRequest) -> Dict:
        """Calculates the first challenge"""
        data = request.json
        input_data = self.__validate_data(data=data)
        splited_number = input_data / 3
        first_part = self.__first_process(number=splited_number)
        second_part = self.__second_process(number=splited_number)
        result = splited_number + first_part + second_part
        return self.__format_response(result=result)

    def __first_process(self, number: float) -> float:
        result = (((number / 4) + 7) ** 2) * 0.257
        return result

    def __second_process(self, number: float) -> float:
        result = ((number**2.121) / 5) + 1
        return result

    def __validate_data(self, data: Dict) -> float:
        if "number" not in data:
            raise ValueError("Number is required!")
        input_data = data.get("number")
        if not isinstance(input_data, (float, int)):
            raise ValueError("Number should be float or integer")
        return input_data

    def __format_response(self, result: float) -> Dict:
        return {"data": {"calculator": 1, "result": round(result, 2)}}
