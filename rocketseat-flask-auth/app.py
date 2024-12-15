""" This is the main file of the project. """
import re
from flask import Flask, request, make_response
from database import db
from models.users import User

app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)

@app.route("/signup", methods=["POST"])
def signup():
    """This is the signup route."""
    data = request.get_json()
    if not data:
        return make_response(
            {
                "message": "You should provide a username and a password to create a User.",
                "error": True,
            },
            400,
        )
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    if not username:
        return make_response(
            {"message": "You should provide a username.", "error": True}, 400
        )
    if not password:
        return make_response(
            {"message": "You should provide a password.", "error": True}, 400
        )
    if not email:
        return make_response(
            {"message": "You should provide an email.", "error": True}, 400
        )
    
    if not isinstance(username, str):
        return make_response(
            {"message": "The username should be a string.", "error": True}, 400
        )
    if not isinstance(password, str):
        return make_response(
            {"message": "The password should be a string.", "error": True}, 400
        )
    if not isinstance(email, str):
        return make_response(
            {"message": "The email should be a string.", "error": True}, 400
        )
    if len(username) < 4 or len(username) > 32:
        return make_response(
            {
                "message": "The username should have between 4 and 32 characters.",
                "error": True,
            },
            400,
        )
    if len(password) < 6 or len(password) > 32:
        return make_response(
            {
                "message": "The password should have between 6 and 32 characters.",
                "error": True,
            },
            400,
        )
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email) or len(email)>64:
        return make_response(
            {"message": "The email should be valid.", "error": True}, 400
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
                400,
            )
        if user and user.email == email:
            return make_response(
                {
                    "message": "The email is already in use.",
                    "error": True,
                },
                400,
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
                201,
            )
        except Exception as e:
            print(e)
            return make_response(
                {
                    "message": "An error occurred while creating the user.",
                    "error": True,
                },
                500,
            )


if __name__ == "__main__":
    app.run(debug=True, port=4444)
