"""This is the module responsible to create each blueprint for the calculator challenge"""

from http import HTTPStatus, HTTPMethod
from flask import Blueprint, request, jsonify
from src.calculators.calculator_1 import FirstCalculator

calc_routes_bp = Blueprint("calc_routes", __name__, url_prefix="/calculators")


@calc_routes_bp.route("/first", methods=[HTTPMethod.POST])
def first_calculator():
    """This is the route controller for the first calculator problem"""
    calculator = FirstCalculator()
    result = calculator.calculate(request=request)
    return jsonify(result), HTTPStatus.OK
