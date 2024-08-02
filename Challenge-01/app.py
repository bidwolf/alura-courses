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


def find_contact():
    """
    Função responsável por achar um contato existente
    """
    name = str(input("Digite o nome do contato\n"))
    for contact in contacts:
        contact_name = contact["name"]
        if name is contact_name or name == contact_name:
            return contact
    raise ContactException(
        message="Nenhum contato com esse nome encontrado", error="NOTFOUND"
    )


def change_contact():
    """
    Função responsável por alterar os dados de um contato
    """
    contact = find_contact()
    print(
        """
Caso não deseje alterar o campo basta apenas apertar a tecla
<Enter> sem preencher o campo em questão\n"""
    )
    new_name = str(input("Nome do contato:(Pressione <ENTER> para pular)\n"))
    new_phone_number = str(input("Telefone:(Pressione <ENTER> para pular)\n"))
    new_mail = str(input("Email do contato:(Pressione <ENTER> para pular)\n"))
    if not new_name and not new_mail and not new_phone_number:
        print("Nenhuma alteração foi feita")
        return
    contact["name"] = new_name if new_name else contact["name"]
    contact["phoneNumber"] = (
        new_phone_number if new_phone_number else contact["phoneNumber"]
    )
    contact["mail"] = new_mail if new_mail else contact["mail"]
    print("Contato alterado com sucesso")
    return


def show_all_contacts():
    """
    Função responsável por listar todos os contatos existentes
    """
    print("CODE\tNAME\tPHONE\tFAVORITE ")
    for index, contact in enumerate(contacts):
        name = contact["name"]
        mail = contact["mail"]
        phoneNumber = contact["phoneNumber"]
        isFavorite = "✔️" if contact["isFavorite"] else "x"
        print(f"{index}\t{name}\t{mail}\t{phoneNumber}\t{isFavorite}")
