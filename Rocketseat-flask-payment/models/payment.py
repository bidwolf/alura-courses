from repository.database import db
from sqlalchemy.orm import Mapped, mapped_column


class Payment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
