"""This is a module for utilities"""

import re
import bcrypt


def is_valid_email(email: str) -> bool:
    """Validate a email format"""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(email) <= 64


def encrypt_password(password: str) -> bytes:
    """Encrypt the password"""
    hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
    return hashed_password


def verify_password(password: str, encrypted_password: str) -> bool:
    """Verify if the password matches the encrypted password"""
    return bcrypt.checkpw(str.encode(password), str.encode(encrypted_password))
