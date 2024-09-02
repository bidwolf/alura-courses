"""This module is responsible for create routes and views for the app"""

import os
import time
from app import app, db
from models import Champions, Users
from src.middlewares.authentication import is_authenticated
from helpers import delete_file, recover_image
from flask import (
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for,
    send_from_directory,
)


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
    return redirect(url_for("login"), code=302)


@app.route("/create-champion")
def create_champion():
    """This is the route that allows the user add a favorite champion"""
    return render_template("create_champion.html")


@app.route("/update-champion/<int:champion_id>")
def update_champion(champion_id):
    """This is the route that allows the user add a favorite champion"""
    if not is_authenticated():
        return redirect(url_for("login"), code=422)
    existent_champion = Champions.query.filter_by(id=champion_id).first()
    splash_art = recover_image(cover_id=champion_id)
    return render_template(
        "update_champion.html", champion=existent_champion, splash_art=splash_art
    )


@app.route("/update", methods=["POST"])
def update():
    """This is the endpoint to update a champion"""
    if not is_authenticated():
        return redirect(url_for("login"), code=422)
    lane = request.form["champion_lane"]
    name = request.form["champion_name"]
    champion_id = request.form["champion_id"]
    rows_changed = Champions.query.filter_by(id=champion_id).update(
        dict(lane=lane, champion_name=name)
    )
    if rows_changed:
        uploaded_file = request.files["splash_art"]
        if uploaded_file:
            timestamp = time.time()
            delete_file(champion_id)
            upload_path = app.config["UPLOAD_PATH"]
            uploaded_file.save(
                f"{upload_path}/splash_art-{champion_id}-{timestamp}.jpg"
            )
        db.session.commit()
        flash("Campeão atualizado com sucesso!")
        return redirect("/", code=302)
    else:
        db.session.flush()
        flash("Something wrong, cannot update champion.\nPlease, try again later.")


@app.route("/delete/<int:champion_id>")
def delete_champion(champion_id):
    """This is the route that allows the user to remove a favorite champion"""
    if not is_authenticated():
        return redirect(url_for("login"), code=422)
    rows_changed = Champions.query.filter_by(id=champion_id).delete()
    if rows_changed:
        delete_file(cover_id=champion_id)
        db.session.commit()
        flash("Champion excluded with success")
        return redirect("/", code=302)
    else:
        db.session.flush()
        flash("Something wrong, cannot delete champion.\nPlease,try again later.")


@app.route("/create", methods=["POST"])
def create():
    """This is the endpoint to create a champion"""
    if not is_authenticated():
        return redirect(url_for("login"), code=422)
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
    uploaded_file = request.files["splash_art"]
    upload_path = app.config["UPLOAD_PATH"]
    if uploaded_file:
        delete_file(new_champion.id)
        timestamp = time.time()
        uploaded_file.save(
            f"{upload_path}/splash_art-{new_champion.id}-{timestamp}.jpg"
        )

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
    return redirect(url_for("login"), code=302)


@app.route("/logout")
def logout():
    """This is the endpoint for logout users"""
    session["user_email"] = None
    flash("User session ended.")
    return redirect("/login")


@app.route("/uploads/<file_name>")
def cover(file_name):
    """Route created to serve the requested image"""
    return send_from_directory(app.config["UPLOAD_PATH"], file_name)
