"""The main application"""

from flask import Flask, render_template, request, redirect, session, flash

from src.models.champion import Champion

app = Flask(__name__)
app.secret_key = "bdiwlof"
nunu = Champion(name="Nunu & Willump", lane="jungle")
viego = Champion(name="Viego", lane="jungle")
jhin = Champion(name="Jhin", lane="Bottom lane")
favorite_champions = [nunu, jhin, viego]


def is_authenticated():
    """Middleware to tell if the user is authenticated"""
    return session.get("user_email") is not None


@app.route("/")
def champion():
    """This is the route that get the champion information"""
    game_name = "League of Legends"
    if is_authenticated():
        return render_template(
            "champion.html",
            game_name=game_name,
            champions=favorite_champions,
            user_email=session.get("user_email"),
        )
    return redirect("/login", 302)


@app.route("/create-champion")
def create_champion():
    """This is the route that allows the user add a favorite champion"""
    return render_template("create_champion.html")


@app.route("/create", methods=["POST"])
def create():
    """This is the endpoint to create a champion"""
    if not is_authenticated():
        return redirect("/login", 422)
    lane = request.form["champion_lane"]
    name = request.form["champion_name"]
    new_champion = Champion(lane=lane, name=name)
    favorite_champions.append(new_champion)
    return redirect("/", code=302)


@app.route("/login")
def login():
    """This is the endpoint to create a session for the web app"""
    return render_template("login.html")


@app.route("/authenticate", methods=["POST"])
def auth():
    """This is the endpoint for authenticate users"""
    mail = request.form["user_email"]
    password = request.form["password"]
    if mail == "tec.henriquedepaula@gmail.com" and password == "123":
        session["user_email"] = mail
        flash("Authentication succeed with success")
        return redirect("/", code=302)

    flash("Authentication failed")
    return redirect("/login", code=302)


@app.route("/logout")
def logout():
    """This is the endpoint for logout users"""
    session["user_email"] = None
    flash("User session ended.")
    return redirect("/login")


app.run(debug=True, port=8080)
