""" This is the main file of the project. """

import datetime
from flask import Flask, request, make_response
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    logout_user,
    login_required,
)
from database import db
from models.users import User
from utils import is_valid_email
import http

app = Flask(__name__)
app.config.from_pyfile("config.py")

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(
        {
            "message": "You should be logged in to access this route.",
            "error": True,
        },
        http.HTTPStatus.UNAUTHORIZED,
    )


@app.errorhandler(400)
def bad_request(error):
    return make_response(
        {
            "message": "Bad request.",
            "error": True,
        },
        http.HTTPStatus.NOT_FOUND,
    )


@app.errorhandler(http.HTTPStatus.NOT_FOUND)
def not_found(error):
    return make_response(
        {
            "message": "Content Not Found.",
            "error": True,
        },
        http.HTTPStatus.NOT_FOUND,
    )


@app.route("/user", methods=["POST"])
def signup():
    """This is the signup route."""
    data = request.get_json()
    if not data:
        return make_response(
            {
                "message": "You should provide a username and a password to create a User.",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    if not username:
        return make_response(
            {"message": "You should provide a username.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if not password:
        return make_response(
            {"message": "You should provide a password.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if not email:
        return make_response(
            {"message": "You should provide an email.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )

    if not isinstance(username, str):
        return make_response(
            {"message": "The username should be a string.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if not isinstance(password, str):
        return make_response(
            {"message": "The password should be a string.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if not isinstance(email, str):
        return make_response(
            {"message": "The email should be a string.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if len(username) < 4 or len(username) > 32:
        return make_response(
            {
                "message": "The username should have between 4 and 32 characters.",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    if len(password) < 6 or len(password) > 32:
        return make_response(
            {
                "message": "The password should have between 6 and 32 characters.",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    if not is_valid_email(email):
        return make_response(
            {"message": "The email should be valid.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if username and password and email:
        user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if user and user.username == username:
            return make_response(
                {
                    "message": "The username is already in use.",
                    "error": True,
                },
                http.HTTPStatus.CONFLICT,
            )
        if user and user.email == email:
            return make_response(
                {
                    "message": "The email is already in use.",
                    "error": True,
                },
                http.HTTPStatus.CONFLICT,
            )
        try:
            user = User(username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()
            return make_response(
                {
                    "message": "User created successfully.",
                    "error": False,
                },
                http.HTTPStatus.CREATED,
            )
        except Exception as e:
            print(e)
            return make_response(
                {
                    "message": "An error occurred while creating the user.",
                    "error": True,
                },
                http.HTTPStatus.INTERNAL_SERVER_ERROR,
            )


@app.route("/user/<int:user_id>", methods=["GET"])
@login_required
def get_user(user_id):
    """This is the get user route."""
    if not isinstance(user_id, int):
        return make_response(
            {
                "message": "You should provide an integer value for user ID.",
                "error": True,
            }
        )
    try:
        user = User.query.get(user_id)
        if not user:
            return make_response(
                {
                    "message": "User not found.",
                    "error": True,
                },
                http.HTTPStatus.NOT_FOUND,
            )
        return make_response(
            {
                "username": user.username,
                "email": user.email,
                "error": False,
                "message": "User found successfully.",
            },
            http.HTTPStatus.OK,
        )
    except Exception as e:
        print(e)
        return make_response(
            {
                "message": "An error occurred while getting the user.",
                "error": True,
            },
            http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@app.route("/user/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id):
    """This is the update user route."""
    data = request.get_json()
    if not data:
        return make_response(
            {
                "message": "You should provide a data to update the user information",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    new_email = data.get("email")
    new_password = data.get("password")
    if not new_password and not new_email:
        return make_response(
            {
                "message": "You should provide a data to update the user information",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    if not isinstance(user_id, int):
        return make_response(
            {
                "message": "You should provide an integer value for user ID.",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    try:
        user = db.session.query(User).get(user_id)
        if user_id != current_user.id:
            return make_response(
                {
                    "message": "You don't have permission to update this user.",
                    "error": True,
                },
                http.HTTPStatus.FORBIDDEN,
            )
        if not user:
            return make_response(
                {"message": "User not found.", "error": True}, http.HTTPStatus.NOT_FOUND
            )
        if new_email and user.email != new_email:
            if not is_valid_email(new_email):
                return make_response(
                    {"message": "The email should be valid.", "error": True},
                    http.HTTPStatus.BAD_REQUEST,
                )
            existent_email_query = (
                db.session.query(User).filter(User.email == new_email).first()
                is not None
            )
            if existent_email_query:
                return make_response(
                    {
                        "message": "This email is already registered by someone else, please check the email provided.",
                        "error": True,
                    },
                    http.HTTPStatus.CONFLICT,
                )
        if new_password:
            if len(new_password) < 6 or len(new_password) > 32:
                return make_response(
                    {
                        "message": "The password should have between 6 and 32 characters.",
                        "error": True,
                    },
                    http.HTTPStatus.BAD_REQUEST,
                )
        user.password = new_password if new_password else user.password
        user.email = new_email if new_email else user.email
        db.session.commit()
        updated_at = datetime.datetime.now()
        return make_response(
            {
                "message": "User updated successfully.",
                "error": False,
                "user": {
                    "email": user.email,
                    "id": user.id,
                    "username": user.username,
                },
                "updated_at": updated_at,
            },
            http.HTTPStatus.CREATED,
        )
    except Exception as e:
        print(e)
        return make_response(
            {"message": "Something went wrong while updating the user.", "error": True}
        )


@app.route("/user/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    """This is the delete user route."""
    if not isinstance(user_id, int):
        return make_response(
            {
                "message": "You should provide an integer value for user ID.",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    try:
        user = db.session.query(User).get(user_id)
        if not user:
            return make_response(
                {"message": "User not found.", "error": True}, http.HTTPStatus.NOT_FOUND
            )
        if user_id != current_user.id:
            return make_response(
                {
                    "message": "You don't have permission to delete this user.",
                    "error": True,
                },
                http.HTTPStatus.FORBIDDEN,
            )
        db.session.delete(user)
        db.session.commit()
        return make_response("", http.HTTPStatus.NO_CONTENT)
    except Exception as e:
        print(e)
        return make_response(
            {"message": "Something went wrong while updating the user.", "error": True}
        )


@app.route("/login", methods=["POST"])
def login():
    """This is the login route."""
    data = request.get_json()
    if not data:
        return make_response(
            {
                "message": "You should provide a username and a password to login.",
                "error": True,
            },
            http.HTTPStatus.BAD_REQUEST,
        )
    username = data.get("username")
    password = data.get("password")
    if not username:
        return make_response(
            {"message": "You should provide a username.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if not password:
        return make_response(
            {"message": "You should provide a password.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if not isinstance(username, str):
        return make_response(
            {"message": "The username should be a string.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if not isinstance(password, str):
        return make_response(
            {"message": "The password should be a string.", "error": True},
            http.HTTPStatus.BAD_REQUEST,
        )
    if username and password:
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return make_response(
                {
                    "message": "Username or password invalid.",
                    "error": True,
                },
                http.HTTPStatus.UNAUTHORIZED,
            )
        login_user(user)
        return make_response(
            {
                "message": "User logged in successfully.",
                "error": False,
            },
            http.HTTPStatus.OK,
        )


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return make_response(
        {
            "message": "User logged out successfully.",
            "error": False,
        },
        http.HTTPStatus.OK,
    )


if __name__ == "__main__":
    app.run(debug=True, port=4444)
