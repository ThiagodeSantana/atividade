
i= 0
soma = 0
n = int(input("numero aluno:"))
while i < n:
    nota= int(input("nota:"))
    soma = soma + nota
    i = i + 1

media = soma/n
print(media)
