"""This module contains the User model."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from database import db


class User(db.Model, UserMixin):
    """This is the User model."""

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(
        String(length=32), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String(length=64), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(length=32), nullable=False)
    def check_password(self,password:str)->bool:
        return self.password==password
