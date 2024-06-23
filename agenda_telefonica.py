def adicionar_contato(contatos, nome_contato, telefone, email):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado com sucesso.")
    return


def visualizar_contatos(contatos):
    print("Estes são seus contatos salvos.")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "☆" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{favorito}] Nome: {nome_contato} Telefone: {telefone_contato} Email: {email_contato}")
    return


def editar_contato(contatos, indice_contatos, atualizacao):
    indice_atualizado = int(indice_contatos) - 1
    if indice_atualizado >= 0 and indice_atualizado < len(contatos):
        if atualizacao == "1":
            novo_nome = input("Qual novo nome deseja: ")
            contatos[indice_atualizado]["nome"] = novo_nome
            print(f"O nome do contato foi atualizado para {novo_nome}")

        elif atualizacao == "2":
            novo_telefone = input("Qual o novo telefone: ")
            contatos[indice_atualizado]["telefone"] = novo_telefone
            print(f"O telefone do contato foi atualizado para {novo_telefone}")
        else:
            novo_email = input("Qual o novo email: ")
            contatos[indice_atualizado]["email"] = novo_email
            print(f"O email do contato foi atualizado para {novo_email}")
        return
    else:
        print("Indice informado invalido.")
        

def salvar_favorito(contatos, indice_contatos):
    indice_atualizado = int(indice_contatos) - 1
    contatos[indice_atualizado]["favorito"] = True
    nome_contato = contatos[indice_atualizado]["nome"]
    print(f"Contato {nome_contato}, foi adicionado como favorito")
    return

def visualizar_favorito(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"] == True:
            favorito = "☆" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"{indice}. [{favorito}] Nome: {nome_contato} Telefone: {telefone_contato} Email: {email_contato}")
    return


def excluir_contato(contatos, indice_contatos):
    indice_atualizado = int(indice_contatos) - 1
    if indice_atualizado >=0 and indice_atualizado <  len(contatos):
        contatos.pop(indice_atualizado)
        print(f"O contato foi removido com sucesso.")


contatos = []
while True:
    print("-=" * 14)
    print("     Lista de contatos.")
    print("-=" * 14)
    print("1- Adicionar contato.")
    print("2- Visualizar contatos")
    print("3- Editar um contato")
    print("4- Marcar contato como favorito")
    print("5- Ver contatos favoritos")
    print("6- Excluir um contato")
    print("7- Sair")
    escolha = input("Qual opção deseja: ")

    if escolha == "1":
        nome_contato = input("Qual o nome do contato que deseja adicionar: ")
        telefone = input("Qual o numero de telefone: ")
        email = input("Qual o email do contato: ")
        adicionar_contato(contatos, nome_contato, telefone, email)

    elif escolha == "2":
        visualizar_contatos(contatos)

    elif escolha == "3":
        visualizar_contatos(contatos)
        indice_contatos = input("Qual contato deseja atualizar: ")
        atualizacao = input(
            "Qual informação deseja atualizar: [1] Nome [2] Telefone [3] Email: ")
        editar_contato(contatos, indice_contatos, atualizacao)

    elif escolha == "4":
        visualizar_contatos(contatos)
        indice_contatos = input("Qual contato deseja salvar como favorito: ")
        salvar_favorito(contatos, indice_contatos)

    elif escolha == "5":
        visualizar_favorito(contatos)
    

    elif escolha == "6":
        visualizar_contatos(contatos)
        indice_contatos = input("Qual contatao deseja excluir: ")
        excluir_contato(contatos, indice_contatos)

    if escolha == "7":
        break
print("Finalizado com sucesso.")
