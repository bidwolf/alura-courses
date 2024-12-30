"""PIX module"""

from uuid import uuid4
from typing import Dict
import qrcode


class Pix:
    """This is the class that represents a payment method"""

    static_folder = "static/img"
    __hash_prefix = "hash_payment_"
    __file_path_prefix = "qr_code_payment_"

    def __init__(self):
        pass

    def get_qrcode_filepath_from_id(self, bank_payment_id):
        """This method return the qrcode path from the given bank institution id"""
        return f"{self.__file_path_prefix}{bank_payment_id}"

    def create_payment(self, base_dir="") -> Dict[str, str]:
        """This method creates a new payment"""
        bank_payment_id = str(uuid4())
        hash_payment = f"{self.__hash_prefix}{bank_payment_id}"
        img = qrcode.make(hash_payment)
        qrcode_path = self.get_qrcode_filepath_from_id(bank_payment_id=bank_payment_id)
        img.save(Pix.get_qrcode_png(filename=qrcode_path, base_dir=base_dir))
        return {"qrcode_path": qrcode_path, "bank_payment_id": bank_payment_id}

    @staticmethod
    def get_qrcode_png(filename: str, base_dir="") -> str:
        """Return the path of the qrcode image"""
        return f"{base_dir}{Pix.static_folder}/{filename}.png"
