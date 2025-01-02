import pytest
from typing import Dict
from .calculator_1 import FirstCalculator

calculator = FirstCalculator()


class MockRequest:
    def __init__(self, body: Dict):
        self.json = body


def test_calculate():
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

    with pytest.raises(ValueError) as exception_info:
        mocked_request = MockRequest({})
        calculator.calculate(mocked_request)
    assert str(exception_info.value) == "Number is required!"


def test_calculate_with_invalid_number_field():

    with pytest.raises(ValueError) as exception_info:
        mocked_request = MockRequest({"number": "a"})
        calculator.calculate(mocked_request)
    assert str(exception_info.value) == "Number should be float or integer"
