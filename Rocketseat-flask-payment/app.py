from flask import Flask, request, jsonify
from http import HTTPStatus
from repository.database import db
from datetime import datetime, timedelta
from models.payment import Payment

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)
PAYMENT_EXPIRATION_DELTA_IN_MINUTES = 30


@app.route("/payments/pix", methods=["POST"])
def create_payment():

    data = request.get_json()
    payment_value: float = data.get("value")
    if isinstance(payment_value, int):
        payment_value = float(payment_value)
    if not data or not payment_value or not isinstance(payment_value, float):
        return (
            jsonify({"message": "Payment should have a value"}),
            HTTPStatus.BAD_REQUEST,
        )
    if payment_value < 0.0:
        return (
            jsonify({"message": "Payment should be greater than 0!"}),
            HTTPStatus.BAD_REQUEST,
        )
    expiration_date = datetime.now() + timedelta(
        minutes=PAYMENT_EXPIRATION_DELTA_IN_MINUTES
    )
    new_payment = Payment(value=data.get("value"), expiration_date=expiration_date)
    db.session.add(new_payment)
    db.session.commit()
    return (
        jsonify(
            {
                "message": "Payment created successfully",
                "payment": new_payment.to_dict(),
            }
        ),
        HTTPStatus.CREATED,
    )


@app.route("/payments/pix/confirmation", methods=["POST"])
def confirm_payment():
    pass


@app.route("/payments/pix/qrcode/<filename>", methods=["GET"])
def get_qrcode(filename: str):
    pass


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def get_payment(payment_id: int):
    pass


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    app.run(debug=True, port=app.config["FLASK_RUN_PORT"])
