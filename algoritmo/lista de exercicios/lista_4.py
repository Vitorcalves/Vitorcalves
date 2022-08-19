# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
from ast import Not


caract = list(input("insira os caracteres: ") for x in range(10))
conso = list()
vogais = ["A", "E", "I", "O", "U"]
cont = 0
for x in range(len(caract)):
    if caract[x].upper() not in vogais:
        conso.insert(1, caract[x])
        cont += 1
print("as consoantes digitadas ",conso)
print("o total de consoantes e ", cont)
