"""This module contains the User model."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from database import db
from utils import verify_password


class User(db.Model, UserMixin):
    """This is the User model."""

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(
        String(length=80), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String(length=80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(length=80), nullable=False)
    role: Mapped[str] = mapped_column(String(length=80), nullable=False, default="user")

    def check_password(self, password: str) -> bool:
        """Check if the given password is valid"""
        return verify_password(encrypted_password=self.password, password=password)
