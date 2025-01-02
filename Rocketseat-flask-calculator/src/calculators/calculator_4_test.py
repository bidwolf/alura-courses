"""This module is responsible for unit tests involving the second calculator"""

from typing import Dict
import pytest
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .calculator_4 import FourthCalculator


class MockRequest:
    """Mock for request purposes"""

    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    """Mock for driver purposes"""

    def __init__(self):
        pass

    def standard_derivation(self, numbers):
        return 3

    def variance(self, numbers):
        return 1

    def average(self, numbers):
        return 1


def test_calculate_integration_with_numpy():
    """Should calculator works properly with right data"""
    calculator = FourthCalculator(driver=NumpyHandler)
    mocked_request = MockRequest({"numbers": [3, 3, 3, 3]})
    response = calculator.calculate(request=mocked_request)
    print(response)
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]
    assert response["data"]["result"] == 3


def test_calculate():
    """Should calculator works properly with right data"""
    calculator = FourthCalculator(driver=MockDriverHandler)
    mocked_request = MockRequest({"numbers": [0.1, 0.2, 0.5, 0.8]})
    response = calculator.calculate(request=mocked_request)
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]
    assert response["data"]["result"] == 1


def test_calculate_without_body():
    """
    Should calculator raises an error when the numbers field is not present in the request body
    """
    calculator = FourthCalculator(driver=MockDriverHandler)
    mocked_request = MockRequest({})
    with pytest.raises(HttpBadRequestError) as exception_info:
        calculator.calculate(mocked_request)
    assert (
        str(exception_info.value)
        == "The request body should have a field called numbers"
    )


def test_calculate_with_invalid_numbers_field():
    """Should calculator raises an error when the numbers field is not a list"""
    calculator = FourthCalculator(driver=MockDriverHandler)
    mocked_request = MockRequest({"numbers": 12})
    with pytest.raises(HttpBadRequestError) as exception_info:
        calculator.calculate(mocked_request)
    assert str(exception_info.value) == "The numbers field should be a list of numbers"


def test_calculate_with_zero_elements_in_numbers_list():
    """Should calculator raises an error when the numbers field not have any number"""
    calculator = FourthCalculator(driver=MockDriverHandler)
    mocked_request = MockRequest({"numbers": []})
    with pytest.raises(HttpBadRequestError) as exception_info:
        calculator.calculate(mocked_request)
    assert (
        str(exception_info.value) == "The numbers field should have at least one number"
    )


def test_calculate_with_invalid_element_in_numbers_list():
    """Should calculator raises an error when the numbers field is not a list"""
    calculator = FourthCalculator(driver=MockDriverHandler)
    mocked_request = MockRequest({"numbers": [12, 13.0, "aa"]})
    with pytest.raises(HttpUnprocessableEntityError) as exception_info:
        calculator.calculate(mocked_request)
    assert (
        str(exception_info.value)
        == "Calculator can't make operations in non numeric arguments"
    )
