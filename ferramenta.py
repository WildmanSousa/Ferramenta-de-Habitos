# organizador_simples.py
# Ferramenta básica de organização pessoal (modo texto)

titulos = []
descricoes = []
datas = []
status = []

# Exibir o menu
def menu():
    print("\n=== MENU DO ORGANIZADOR ===")
    print("1 - Cadastrar nova tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar status")
    print("4 - Pesquisar tarefa")
    print("5 - Remover tarefa")
    print("6 - Sair")

# Cadastrar nova tarefa
def cadastrar():
    print("\n--- Cadastrar Tarefa ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data = input("Data (DD/MM/AAAA): ")

    titulos.append(titulo)
    descricoes.append(descricao)
    datas.append(data)
    status.append("pendente")

    print("Tarefa cadastrada com sucesso!")

# Listar todas as tarefas
def listar():
    print("\n--- Lista de Tarefas ---")
    if len(titulos) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    for i in range(len(titulos)):
        print(f"\nID: {i}")
        print("Título:", titulos[i])
        print("Descrição:", descricoes[i])
        print("Data:", datas[i])
        print("Status:", status[i])

# Atualizar status de uma tarefa
def atualizar():
    listar()
    try:
        i = int(input("\nDigite o ID da tarefa para atualizar: "))
        if 0 <= i < len(status):
            novo = input("Novo status (pendente/concluído): ").lower()
            if novo in ["pendente", "concluído"]:
                status[i] = novo
                print("Status atualizado!")
            else:
                print("Status inválido.")
        else:
            print("ID inválido.")
    except:
        print("Erro: entrada inválida.")

# Pesquisar por palavra-chave
def pesquisar():
    palavra = input("\nDigite uma palavra-chave: ").lower()
    encontrou = False
    for i in range(len(titulos)):
        if palavra in titulos[i].lower() or palavra in descricoes[i].lower():
            print(f"\nID: {i}")
            print("Título:", titulos[i])
            print("Descrição:", descricoes[i])
            print("Data:", datas[i])
            print("Status:", status[i])
            encontrou = True
    if not encontrou:
        print("Nenhuma tarefa encontrada com essa palavra.")

# Remover uma tarefa
def remover():
    listar()
    try:
        i = int(input("\nDigite o ID da tarefa para remover: "))
        if 0 <= i < len(titulos):
            print(f"Removendo tarefa: {titulos[i]}")
            confirmar = input("Tem certeza? (s/n): ")
            if confirmar.lower() == "s":
                del titulos[i]
                del descricoes[i]
                del datas[i]
                del status[i]
                print("Tarefa removida.")
            else:
                print("Remoção cancelada.")
        else:
            print("ID inválido.")
    except:
        print("Erro: entrada inválida.")

# Programa principal
opcao = ""
while opcao != "6":
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        pesquisar()
    elif opcao == "5":
        remover()
    elif opcao == "6":
        print("Saindo... Até mais!")
    else:
        print("Opção inválida. Tente novamente.")
