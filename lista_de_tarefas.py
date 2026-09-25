# Lista de Tarefas
tarefas = [
    {'titulo': 'estudar', 'concluida': 'sim', 'prioridade': 'alta'}, 
    {'titulo': 'correr', 'concluida': 'sim', 'prioridade': 'alta'},
    {'titulo': 'ler', 'concluida': 'não', 'prioridade': 'baixa'}
]


def mostrar():
    print(tarefas)


def concluidas():
    for item in tarefas:
        if item['concluida'] == 'sim':
            print(f"Título: {item['titulo']}")

def pendentes():
    for item in tarefas:
        if item['concluida'] == 'não':
            print(f"Título: {item['titulo']}")

def prioridade():
    prioridade = input("Você quer achar por qual prioridade? ")

    for item in tarefas:
        if item ['prioridade'] == prioridade:
            print(f"Título: {item['titulo']}")

def cadastrar():
    print("---> Cadastrando uma nova Tarefa ")
    tarefa = input("Digite a Tarefa: ")
    prioridade_tarefa = input("Digite a Prioridade: ")

    nova_tarefa = {
        'titulo': tarefa,
        'concluida': 'não',
        'prioridade': prioridade_tarefa
    }

    tarefas.append(nova_tarefa)




def finalizar():
    nome = input("Digite o título da tarefa que deseja concluir: ")
    for item in tarefas:
        if item['titulo'] == nome:
            item['concluida'] = 'sim'
            print("Tarefa concluída!")

def remover():
    print("---> Removendo uma Tarefa ")
    tarefa_remover = input("Digite qual tarefa você quer remover: ")

    for item in tarefas:
        if item['titulo'] == tarefa_remover:
            tarefas.remove(item)
            print("Tarefa Removida ")



while True:
    print("Lista de Tarefas")
    print ("1 - Mostrar Tarefas")
    print ("2 - Mostrar Tarefas Concluídas")
    print ("3 - Mostrar Tarefas Pendentes")
    print ("4 - Mostrar Tarefas por Prioridade")
    print ("5 - Cadastrar Tarefa Nova")
    print ("6 - Finalizar Tarefa")
    print ("7 - Remover Tarefa")
    print ("0 - Sair")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        mostrar()

    elif opcao == "2":
        concluidas()

    elif opcao == "3":
        pendentes()

    elif opcao == "4":
        prioridade()

    elif opcao == "5":
        cadastrar()

    elif opcao == "6":
        finalizar()

    elif opcao == "7":
        remover()

    elif opcao == "0":
        print("Saindo do Sistema...")
        break




