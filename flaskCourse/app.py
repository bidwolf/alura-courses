"""The main application"""

from flask import Flask, render_template

# from src.models.champion import Champion

app = Flask(__name__)


@app.route("/champion")
def champion():
    """This is the route that get the champion information"""
    return render_template("champion.html")


app.run(debug=True, port=8080)
