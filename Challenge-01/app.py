"""
Este app é responsável por criar uma aplicação de terminal para cadastro de contatos.
O mesmo segue os requisitos do desafio proposto pela Rocketseat no curso de Python.
Acesse o link para mais informações: https://efficient-sloth-d85.notion.site/Desafio-01-622bb29769034c9ba659f2dc33019055
"""


class ContactException(Exception):
    """
    Exceções para contatos
    """

    def __init__(self, message, error):
        super().__init__(message)
        self.error = error
