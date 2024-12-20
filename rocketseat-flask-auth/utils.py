"""This is a module for utilities"""
import re
def is_valid_email(email:str)->bool:
    """Validate a email format"""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(email) <= 64
