"""This module contains the logic to handle flask errors"""

from typing import Dict
from http import HTTPStatus
from .http_bad_request import HttpBadRequestError
from .http_unprocessable_entity import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> Dict:
    """Handle personalized errors for each request"""
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {"title": error.name, "details": error.message},
        }
    return {
        "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
        "body": {
            "title": "Internal Server Error",
            "details": "Server got itself in trouble",
        },
    }
