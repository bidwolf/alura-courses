"""The main application"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
csrf = CSRFProtect(app=app)
from views import *


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("APP_PORT"))
