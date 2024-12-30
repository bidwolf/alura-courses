from datetime import datetime
from sqlalchemy import Integer, Float, Boolean, String, DateTime
from repository.database import db, Base
from sqlalchemy.orm import Mapped, mapped_column


class Payment(Base):
    __tablename__ = "payment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[float] = mapped_column(Float)
    paid: Mapped[bool] = mapped_column(Boolean, default=False)
    bank_payment_id: Mapped[str] = mapped_column(String(100), nullable=True)
    qrcode: Mapped[str] = mapped_column(String(100), nullable=True)
    expiration_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qrcode": self.qrcode,
            "expiration_date": self.expiration_date,
        }
