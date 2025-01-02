"""This is the module responsible to create each blueprint for the calculator challenge"""

from http import HTTPStatus, HTTPMethod
from flask import Blueprint, request, jsonify
from src.main.factories.calculator_factory import calculator_factory
from src.errors.error_controller import handle_errors

calc_routes_bp = Blueprint("calc_routes", __name__, url_prefix="/calculators")


@calc_routes_bp.route("/first", methods=[HTTPMethod.POST])
def first_calculator():
    """This is the route controller for the first calculator problem"""
    try:
        calculator = calculator_factory(calculator_type="first")
        result = calculator.calculate(request=request)
        return jsonify(result), HTTPStatus.OK
    except Exception as exception:
        error_response = handle_errors(error=exception)
        return jsonify(error_response), error_response["status_code"]


@calc_routes_bp.route("/second", methods=[HTTPMethod.POST])
def second_calculator():
    """This is the route controller for the second calculator problem"""
    try:
        calculator = calculator_factory(calculator_type="second")
        result = calculator.calculate(request=request)
        return jsonify(result), HTTPStatus.OK
    except Exception as exception:
        error_response = handle_errors(error=exception)
        return jsonify(error_response), error_response["status_code"]


@calc_routes_bp.route("third", methods=[HTTPMethod.POST])
def third_calculator():
    """
    This is the route controller for the third calculator problem
    """
    try:
        calculator = calculator_factory(calculator_type="third")
        result = calculator.calculate(request=request)
        return jsonify(result), HTTPStatus.OK
    except Exception as exception:
        error_response = handle_errors(error=exception)
        return jsonify(error_response), error_response["status_code"]
