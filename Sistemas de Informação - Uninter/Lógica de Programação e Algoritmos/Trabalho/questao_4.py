# Mensagem de boas vindas
print("Bem-vindo(a) à Lista de Contados do Nycolas Felipe Lourenço")


# Lista de contatos e id RU
lista_contatos = []
id_global = 5045736


# Função para cadastrar novos contatos
def cadastrar_contato(id):
    # Acessa a lista global de contatos
    global lista_contatos

    # Recebe informações do usuário
    nome = input("Por favor entre o nome do contato: ")
    atividade = input("Por favor entre com a atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")
    print()

    # Cadastra novo contato com as informações obtidas
    contato = { 'id': id, 'nome': nome, 'atividade': atividade, 'telefone': telefone }
    lista_contatos = lista_contatos.copy() + [contato]

    print("Contato adicionado com sucesso!")
    print()


# Função para consultar todos os contatos, contatos por id e por atividade
def consultar_contatos():
    # Acessa a lista global de contatos
    global lista_contatos

    # Inicia menu para consulta de contatos
    while True:
        print("-----------------------------------------------------------")
        print("----------------- MENU CONSULTAR CONTATOS -----------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar todos os contatos")
        print("2 - Consultar contato por id")
        print("3 - Consultar contato(s) por atividade")
        print("4 - Retornar")

        opcao = input(">> ")
        print()

        # Retorna lista de todos os contatos
        if opcao == "1":
            for contato in lista_contatos:
                print(f"Id: {contato['id']}")
                print(f"Nome: {contato['nome']}")
                print(f"Atividade: {contato['atividade']}")
                print(f"Telefone: {contato['telefone']}")
                print()
        
        # Retorna contato com id específico
        elif opcao == "2":
            print("Informe o id do contato:")
            id = int(input(">> "))
            print()

            contato_encontrado = False

            for contato in lista_contatos:
                if contato['id'] == id:
                    print(f"Id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    contato_encontrado = True
                    print()
            
            if not contato_encontrado:
                print("Não existe contato com o id informado.")
                print()
        
        # Retorna lista de contatos com atividade específica
        elif opcao == "3":
            print("Informe a atividade do contato:")
            atividade = input(">> ")
            print()

            contato_encontrado = False

            for contato in lista_contatos:
                if contato['atividade'] == atividade:
                    print(f"Id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    contato_encontrado = True
                    print()
            
            if not contato_encontrado:
                print("Não existe contato com a atividade informada.")
                print()
        
        # Retorna ao menu principal
        elif opcao == "4":
            return
        
        # Opção inválida, retorna ao começo do menu de consulta
        else:
            print("Opção inválida.")
            print()
            continue


# Função para remover contato por id
def remover_contato():
    # Acessa a lista global de contatos
    global lista_contatos

    # Inicia menu para remover contato
    while True:
        print("-----------------------------------------------------------")
        print("------------------- MENU REMOVER CONTATO ------------------")
        print("Escolha a opção desejada:")
        print("1 - Remover contato")
        print("2 - Retornar")

        opcao = input(">> ")
        print()

        # Procura contato com id informado e remove da lista de contatos
        if opcao == "1":
            id = int(input("Informe o id do contato: "))
            print()

            contato_encontrado = False

            for i in range(len(lista_contatos)):
                if lista_contatos[i]['id'] == id:
                    del lista_contatos[i]
                    contato_encontrado = True
                    print("Contato removido com sucesso.")
                    print()
                    return
            
            if not contato_encontrado:
                print("Id inválido. Informe o id novamente.")
                print()
        
        # Retorna ao menu principal
        elif opcao == "2":
            return
        
        # Em caso de opção inválido, retorna ao inicio do menu atual
        else:
            print("Opção inválida.")
            print()
            continue


# Início do menu principal
while True:
    print("-----------------------------------------------------------")
    print("---------------------- MENU PRINCIPAL ---------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar contato")
    print("2 - Consultar contato(s)")
    print("3 - Remover contato")
    print("4 - Sair")

    opcao = input(">> ")
    print()

    # Cadastra novo contato
    if opcao == "1":
        id_global += 1
        cadastrar_contato(id_global)

    #  Consulta contatos
    elif opcao == "2":
        consultar_contatos()

    # Remove contato
    elif opcao == "3":
        remover_contato()

    # Encerra o programa
    elif opcao == "4":
        break
    
    # Opção inválida, retorna ao início do menu
    else:
        print("Opção inválida.")
        print()
        continue
