"""This module contains the personalized error class for unprocessable entity http errors"""

from http import HTTPStatus


class HttpUnprocessableEntityError(Exception):
    """Class responsible to handle the unprocessable entity errors"""

    def __init__(self, message):
        super().__init__(message)
        self.name = "Unprocessable Entity"
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.message = message
