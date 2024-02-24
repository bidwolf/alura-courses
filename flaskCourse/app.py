"""The main application"""

from flask import Flask, render_template, request, redirect

from src.models.champion import Champion

app = Flask(__name__)

nunu = Champion(name="Nunu & Willump", lane="jungle")
viego = Champion(name="Viego", lane="jungle")
jhin = Champion(name="Jhin", lane="Bottom lane")
favorite_champions = [nunu, jhin, viego]


@app.route("/")
def champion():
    """This is the route that get the champion information"""
    game_name = "League of Legends"

    return render_template(
        "champion.html", game_name=game_name, champions=favorite_champions
    )


@app.route("/create-champion")
def create_champion():
    """This is the route that allows the user add a favorite champion"""
    return render_template("create_champion.html")


@app.route("/create", methods=["POST"])
def create():
    """This is the endpoint to create a champion"""
    lane = request.form["champion_lane"]
    name = request.form["champion_name"]
    new_champion = Champion(lane=lane, name=name)
    favorite_champions.append(new_champion)
    return redirect("/", code=302)


app.run(debug=True, port=8080)
