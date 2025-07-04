horas1 = int(input("entrada da hora: "))
minutos1 = int(input("entrada do minuto: "))
horas2 = int(input("entrada da hora: "))
minutos2 = int(input("entrada do minuto: "))

# Soma minutos e ajusta horas se necessário
minutos = minutos1 + minutos2
horas = horas1 + horas2

if minutos >= 60:
    horas += minutos // 60
    minutos = minutos % 60

# Ajusta para formato 24 horas, se necessário
if horas >= 24:
    horas = horas % 24

print(horas, minutos, "horas")  