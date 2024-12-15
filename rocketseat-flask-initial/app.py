""" This is the main file of the project. """

from flask import Flask
from database import db
from models.users import User

app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)


@app.route("/signup", methods=["GET"])
def signup():
    """This is the signup route."""
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, port=3333)
