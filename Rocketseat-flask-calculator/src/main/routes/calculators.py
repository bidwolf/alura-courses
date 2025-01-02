"""This is the module responsible to create each blueprint for the calculator challenge"""

from http import HTTPStatus, HTTPMethod
from flask import Blueprint, request, jsonify
from src.main.factories.calculator_factory import calculator_factory


calc_routes_bp = Blueprint("calc_routes", __name__, url_prefix="/calculators")


@calc_routes_bp.route("/first", methods=[HTTPMethod.POST])
def first_calculator():
    """This is the route controller for the first calculator problem"""
    calculator = calculator_factory(calculator_type="first")
    result = calculator.calculate(request=request)
    return jsonify(result), HTTPStatus.OK


@calc_routes_bp.route("/second", methods=[HTTPMethod.POST])
def second_calculator():
    """This is the route controller for the second calculator problem"""
    calculator = calculator_factory(calculator_type="second")
    result = calculator.calculate(request=request)
    return jsonify(result), HTTPStatus.OK
