"""This is the module for handling models for the application"""

from app import db


class Champions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    champion_name = db.Column(db.String(30), nullable=False)
    lane = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return "<Champion %r>" % self.champion_name


class Users(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
