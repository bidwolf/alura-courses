"""Test module for the first calculator logic"""

from typing import Dict
import pytest
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .calculator_1 import FirstCalculator

calculator = FirstCalculator()


class MockRequest:
    """Mock for request purposes"""

    def __init__(self, body: Dict):
        self.json = body


def test_calculate():
    """Ensure that the calculator works properly with right arguments"""
    mocked_request = MockRequest({"number": 1})
    response = calculator.calculate(mocked_request)
    print()
    print(response)
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]
    assert response["data"]["calculator"] == 1
    assert isinstance(response["data"]["result"], float)
    assert response["data"]["result"] == 14.25


def test_calculate_without_number_in_body():
    """Ensure that the bad request error is raised when a body is not present"""
    with pytest.raises(HttpBadRequestError) as exception_info:
        mocked_request = MockRequest({})
        calculator.calculate(mocked_request)
    assert str(exception_info.value) == "Number is required!"


def test_calculate_with_invalid_number_field():
    """Ensure that the unprocessable entity error is raised when a body is bad formatted"""
    with pytest.raises(HttpUnprocessableEntityError) as exception_info:
        mocked_request = MockRequest({"number": "a"})
        calculator.calculate(mocked_request)
    assert (
        str(exception_info.value)
        == "Calculator can't make operations with a non numeric argument"
    )
