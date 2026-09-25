aluno = {"nome": "ana", "cel": "119536718", "nota": "10"}

clientes = [
    {"nome": "Ana", "cel": "1111", "empresa": "FIAT"},
    {"nome": "Pedro", "cel": "2222", "empresa": "INTEL"},
    {"nome": "Maria", "cel": "3333", "empresa": "SEBRAE"},
    {"nome": "Felipe", "cel": "4444", "empresa": "INTEL"}
]

# Busca por Empresas
pergunta = input("Qual empresa você quer? ")

for cliente in clientes:
    if cliente["empresa"] == pergunta:
        print(cliente["nome"])

# Cadastrar um novo cliente
print("---> Cadastrando Um Novo Cliente")
nome_novo = input("Digite seu nome: ")
cel_novo = input("Digite seu telefone: ")
empresa_nova = input("Digite o nome da sua Empresa: ")

novo_cliente = {
    "nome": nome_novo,
    "cel": cel_novo,  
    "empresa": empresa_nova
}
clientes.append(novo_cliente)
print("Lista após cadastro:", clientes)

# Remover um cliente
print("---> Removendo Um Cliente")
nome_remover = input("Digite o nome do cliente a remover: ")
cel_remover = input("Digite o telefone: ")
empresa_remover = input("Digite a empresa: ")

cliente_para_remover = {
    "nome": nome_remover,
    "cel": cel_remover,
    "empresa": empresa_remover
}

if cliente_para_remover in clientes:
    clientes.remove(cliente_para_remover)
    print("Cliente removido com sucesso!")
else:
    print("Cliente não encontrado na lista.")

print("Lista atualizada:", clientes)