from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import registry

reg = registry()


class Base(DeclarativeBase):
    """Base class for all models"""

    registry = reg


db = SQLAlchemy(model_class=Base)
