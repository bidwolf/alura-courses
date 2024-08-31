from app import app
from models import Champions, Users
from src.middlewares.authentication import is_authenticated
from flask import render_template, request, redirect, session, flash


@app.route("/")
def champion():
    """This is the route that get the champion information"""
    game_name = "League of Legends"
    champions = Champions.query.order_by(Champions.champion_name)
    if is_authenticated():
        return render_template(
            "champion.html",
            game_name=game_name,
            champions=champions,
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
    champion_already_exists = (
        Champions.query.filter_by(champion_name=name).filter_by(lane=lane).first()
    )
    if champion_already_exists:
        flash("Champion already exists")
        return redirect("/", code=302)
    new_champion = Champions(champion_name=name, lane=lane)
    db.session.add(new_champion)
    db.session.commit()
    return redirect("/", code=302)


@app.route("/login")
def login():
    """This is the endpoint to create a session for the web app"""
    return render_template("login.html")


@app.route("/authenticate", methods=["POST"])
def auth():
    """This is the endpoint for authenticate users"""
    username = request.form["user_email"]
    password = request.form["password"]
    user = Users.query.filter_by(username=username).first()
    if user:
        if password == user.password:
            session["user_email"] = username
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
