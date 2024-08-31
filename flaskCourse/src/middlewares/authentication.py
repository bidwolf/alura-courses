"""
This middleware aims to define rules for the app authentication
"""

from flask import session


def is_authenticated():
    """Middleware to tell if the user is authenticated"""
    return "user_email" in session and session.get("user_email") is not None
