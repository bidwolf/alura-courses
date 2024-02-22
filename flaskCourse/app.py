"""The main application"""

from flask import Flask, render_template

from src.models.champion import Champion

app = Flask(__name__)


@app.route("/champion")
def champion():
    """This is the route that get the champion information"""
    game_name = "League of Legends"
    nunu = Champion(name="Nunu & Willump", lane="jungle")
    viego = Champion(name="Viego", lane="jungle")
    jhin = Champion(name="Jhin", lane="Bottom lane")
    favorite_champions = [nunu, jhin, viego]
    return render_template(
        "champion.html", game_name=game_name, champions=favorite_champions
    )


@app.route("/create-champion")
def create_champion():
    """This is the route that allows the user add a favorite champion"""
    return render_template("create_champion.html")


app.run(debug=True, port=8080)
