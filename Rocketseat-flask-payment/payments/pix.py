"""PIX module"""

from uuid import uuid4, UUID
from typing import Dict, Union
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

    def create_payment(self) -> Dict[str, str]:
        """This method creates a new payment"""
        bank_payment_id = str(uuid4())
        hash_payment = f"{self.__hash_prefix}{bank_payment_id}"
        img = qrcode.make(hash_payment)
        qrcode_path = self.get_qrcode_filepath_from_id(bank_payment_id=bank_payment_id)
        img.save(Pix.get_qrcode_png(filename=qrcode_path))
        return {"qrcode_path": qrcode_path, "bank_payment_id": bank_payment_id}

    @staticmethod
    def get_qrcode_png(filename: str) -> str:
        """Return the path of the qrcode image"""
        return f"{Pix.static_folder}/{filename}.png"
