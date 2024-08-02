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


def create_contact():
    """
    Função responsável por criar um contato na lista de contatos
    """
    name = str(print("Nome do contato:\n"))
    phoneNumber = str(print("Telefone:\n"))
    mail = str(print("Nome do contato:\n"))
    print("Contato criado com sucesso")
    new_contact = {
        "name": name,
        "phoneNumber": phoneNumber,
        "mail": mail,
        "isFavorite": False,
    }
    contacts.append(new_contact)


contacts = []  # A lista de contatos existentes
