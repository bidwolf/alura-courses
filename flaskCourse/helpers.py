"""Module for create helpers for the application"""

import os
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import SubmitField, StringField, PasswordField
from app import app


class FlaskChampionForm(FlaskForm):
    """Form for the champion"""

    champion_lane = StringField(
        "Lane", validators=[DataRequired(), Length(min=3, max=10)]
    )
    champion_name = StringField(
        "Champion Name", validators=[DataRequired(), Length(min=3, max=30)]
    )
    submit = SubmitField("Send")


class FlaskLoginForm(FlaskForm):
    """Form for user login"""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=30)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=3, max=100)]
    )
    login = SubmitField("Login")


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
