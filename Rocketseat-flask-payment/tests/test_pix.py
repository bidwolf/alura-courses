import sys

sys.path.append("../")
import pytest
import os
from payments.pix import Pix


def test_pix_create_payment():
    """
    Test the payment method
    - should create_payment method return the bank_payment_id and qrcode
    """
    pix_instance = Pix()
    payment_info = pix_instance.create_payment(base_dir="../")
    qrcode_path = Pix.get_qrcode_png(
        filename=payment_info["qrcode_path"], base_dir="../"
    )
    qrcode_exists = os.path.exists(qrcode_path)
    qrcode_is_file = os.path.isfile(qrcode_path)
    assert "bank_payment_id" in payment_info
    assert "qrcode_path" in payment_info
    assert qrcode_exists is True
    assert qrcode_is_file is True
