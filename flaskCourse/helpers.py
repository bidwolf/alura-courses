"""Module for create helpers for the application"""

import os
from app import app


def recover_image(cover_id):
    """Recover the correct file if exists to serve"""
    upload_path = app.config["UPLOAD_PATH"]
    for file_name in os.listdir(upload_path):
        if f"splash_art-{cover_id}" in file_name:
            return file_name
    return "default_splash_art.png"


def delete_file(cover_id):
    """Delete duplicated file in the uploads folder"""
    file_to_delete = recover_image(cover_id=cover_id)
    if file_to_delete != "default_splash_art.png":
        os.remove(os.path.join(app.config["UPLOAD_PATH"], file_to_delete))
