num = 0
senhac = int(input("digite a senha para salvar:"))
print("_________________")

while num < 3:
    senha = int(input("digite a senha:"))
    print("__________________")

    if senha == senhac:
        print("senha correta")
        break
    else:
        print("senha incorreta")
        num += 1
        print("________________")

if num == 3:
    print("senha bloqueada")