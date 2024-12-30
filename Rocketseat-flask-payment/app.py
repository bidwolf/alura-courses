from flask import Flask, request, jsonify, send_file, render_template
from http import HTTPStatus
from repository.database import db
from datetime import datetime, timedelta
from models.payment import Payment
from payments.pix import Pix
from os import path

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)
PAYMENT_EXPIRATION_DELTA_IN_MINUTES = 30


@app.route("/payments/pix", methods=["POST"])
def create_payment():
    """POST Method to create a payment transaction"""
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
    pix = Pix()
    pix_transaction_details = pix.create_payment()
    new_payment = Payment(
        value=data.get("value"),
        expiration_date=expiration_date,
        qrcode=pix_transaction_details.get("qrcode_path"),
        bank_payment_id=pix_transaction_details.get("bank_payment_id"),
    )
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
    """GET Method to send the qrcode image"""
    directory = Pix.get_qrcode_png(filename=filename)
    if path.exists(directory):
        return send_file(Pix.get_qrcode_png(filename=filename))
    return (
        jsonify({"message": "This image is not present in the server"}),
        HTTPStatus.NOT_FOUND,
    )


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def get_payment(payment_id: int):
    pass


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    app.run(debug=True, port=app.config["FLASK_RUN_PORT"])
