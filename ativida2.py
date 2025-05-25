user = {}

def menu():
    print("1- cadastro")
    print("2- login")
    print("3- sair")
    return int(input("digite o número desejado: "))

def cadastro():
    nome = input("digite seu nome: ")
    senha = int(input("digite sua senha: "))
    idade = int(input("digite sua idade: "))
    user[nome] = {"senha": senha, "idade": idade}
    print("usuário cadastrado com sucesso")

def login():
    nome = input("digite seu nome: ")
    senha = int(input("digite sua senha: "))
    if nome in user and senha == user[nome]["senha"]:
        print("login realizado com sucesso")
    else:
        print("senha incorreta")

def sair():
    print("sair do sistema")

while True:
    opção = menu()
    if opção == 1:
        cadastro()
    elif opção == 2:
        login()
    elif opção == 3:
        sair()
        break