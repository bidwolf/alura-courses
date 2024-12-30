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
    """POST Method to send payment confirmation"""
    data = request.get_json()
    bank_payment_id = data.get("bank_payment_id")
    value = data.get("value")
    if not bank_payment_id:
        return (
            jsonify({"message": "The bank_payment_id is required"}),
            HTTPStatus.BAD_REQUEST,
        )
    if not isinstance(bank_payment_id, str):
        return (
            jsonify({"message": "The bank_payment_id should be a string"}),
            HTTPStatus.BAD_REQUEST,
        )
    if not value:
        return (
            jsonify({"message": "The value is required"}),
            HTTPStatus.BAD_REQUEST,
        )
    if isinstance(value, int):
        value = float(value)
    if not isinstance(value, float):
        return (
            jsonify({"message": "The value should be a float number"}),
            HTTPStatus.BAD_REQUEST,
        )
    payment = (
        db.session.query(Payment)
        .filter(Payment.bank_payment_id == bank_payment_id)
        .first()
    )
    if not payment:
        return (jsonify({"message": "Cannot find this payment"}), HTTPStatus.NOT_FOUND)
    if payment.paid:
        return (
            jsonify({"message": "Payment has already been confirmed"}),
            HTTPStatus.CONFLICT,
        )
    if payment.value != value:
        return (
            jsonify({"message": "Invalid payment data"}),
            HTTPStatus.METHOD_NOT_ALLOWED,
        )
    try:
        payment.paid = True
        db.session.commit()
        return (
            jsonify({"message": "Payment confirmed successfully"}),
            HTTPStatus.ACCEPTED,
        )
    except Exception as e:
        db.session.rollback()
        return (
            jsonify({"message": "An internal error occurred while confirm payment"}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


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
    """Send payment page to the client"""
    try:
        payment = db.session.query(Payment).filter(Payment.id == payment_id).first()
        if not payment:
            return (render_template("404.html"), HTTPStatus.NOT_FOUND)
        return render_template(
            "payment.html",
            payment=payment.to_dict(),
            host=f"http://127.0.0.1:{app.config["FLASK_RUN_PORT"]}",
        )
    except Exception as e:
        return (
            jsonify({"message": "Internal server Error"}),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    app.run(debug=True, port=app.config["FLASK_RUN_PORT"])
