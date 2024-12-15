from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db


class User(db.Model):
    """This is the User model."""

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(
        String(length=32), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String(length=32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(length=32), nullable=False)
