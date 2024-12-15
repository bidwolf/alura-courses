""" This is the main file of the project. """

from flask import Flask, request, make_response
from database import db
from models.users import User

app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)


@app.route("/signup", methods=["GET"])
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
    if not username:
        return make_response(
            {"message": "You should provide a username.", "error": True}, 400
        )
    if not password:
        return make_response(
            {"message": "You should provide a password.", "error": True}, 400
        )
    if not isinstance(username, str):
        return make_response(
            {"message": "The username should be a string.", "error": True}, 400
        )
    if not isinstance(password, str):
        return make_response(
            {"message": "The password should be a string.", "error": True}, 400
        )
    if len(username) < 4:
        return make_response(
            {
                "message": "The username should have at least 4 characters.",
                "error": True,
            },
            400,
        )
    if len(password) < 6:
        return make_response(
            {
                "message": "The password should have at least 6 characters.",
                "error": True,
            },
            400,
        )
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user:
            return make_response(
                {
                    "message": "This user already exists. Please, choose another username.",
                    "error": True,
                },
                400,
            )
        try:
            user = User(username=username, password=password)
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
    app.run(debug=True, port=3333)
