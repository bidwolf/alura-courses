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


def show_only_favorites():
    """
    Função responsável por listar todos os contatos favoritos
    """
    print("CODE\tNAME\tPHONE\tFAVORITE ")
    for index, contact in enumerate(contacts):
        name = contact["name"]
        mail = contact["mail"]
        phoneNumber = contact["phoneNumber"]
        isFavorite = "✔️" if contact["isFavorite"] else "x"
        if isFavorite == "✔️":
            print(f"{index}\t{name}\t{mail}\t{phoneNumber}\t{isFavorite}")


def toggle_favorite_contact():
    """
    Função responsável por marcar/desmarcar um contato como favorito na lista de contatos
    """
    print("Operação concluída com sucesso")
    contact = find_contact()
    contact["isFavorite"] = not contact["isFavorite"]


def delete_contact():
    """
    Função responsável por deletar um contato existente
    """
    name = input("Digite o nome do contato que deseja excluir:\n")
    for index, contact in enumerate(contacts):
        if contact["name"] == name:
            deleted_contact = contacts.pop(index)
            print(f"O contato {name} foi excluido com sucesso\n", deleted_contact)
            return


def main():
    """
    Função principal do app
    """
    print("BEM VINDO AO ROCKET CONTACTS")
    print("O QUE DESEJA FAZER?\n")
    selected_option = 30
    while selected_option != 0:
        print("1 - ADICIONAR CONTATO")
        print("2 - ALTERAR CONTATO EXISTENTE")
        print("3 - LISTAR TODOS OS CONTATOS")
        print("4 - LISTAR FAVORITOS")
        print("5 - MARCAR/DESMARCAR CONTATO COMO FAVORITO")
        print("6 - REMOVER CONTATO")
        print("0 - SAIR")
        try:
            selected_option = int(input())
            if selected_option not in range(0, 6):
                print("Opção inválida")
                continue
            print(f"Você selecionou a opção {selected_option}")
            match selected_option:
                case 1:
                    create_contact()
                case 2:
                    change_contact()
                case 3:
                    show_all_contacts()
                case 4:
                    show_only_favorites()
                case 5:
                    toggle_favorite_contact()
                case 6:
                    delete_contact()
        except ValueError as error:
            print("O valor informado é inválido", error)
        except ContactException as error:
            print(error, error.error)
        except Exception as error:
            print("Ocorreu um erro durante a execução do programa", error)


# INICIO DA APLICAÇÃO

main()
