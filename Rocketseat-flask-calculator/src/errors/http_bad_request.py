"""This module contains the personalized error class for bad request http errors"""

from http import HTTPStatus


class HttpBadRequestError(Exception):
    """Class responsible to handle the bad request errors"""

    def __init__(self, message):
        super().__init__(message)
        self.name = "Bad Request"
        self.status_code = HTTPStatus.BAD_REQUEST
        self.message = message
