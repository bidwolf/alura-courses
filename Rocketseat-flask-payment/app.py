from flask import Flask
from repository.database import db

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)


@app.route("/payments/pix", methods=["POST"])
def create_payment():
    pass


@app.route("/payments/pix/confirmation", methods=["POST"])
def confirm_payment():
    pass


@app.route("/payments/pix/qrcode/<str:filename>", methods=["GET"])
def get_qrcode(filename: str):
    pass


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def get_payment(payment_id: int):
    pass


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    app.run(debug=True)
