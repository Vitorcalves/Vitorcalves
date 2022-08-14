# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
caract = list(input("insira os caracteres: ") for x in range(10))
conso = list("")
cont = 0
for x in range(len(caract)):
    if caract[x].upper == "A" and caract[x].upper == "E" and caract[x].upper == "I" and caract[x].upper == "O" and caract[x].upper == "U":
        conso.insert(1, caract[x])
        cont += 1
print("as consoantes digitadas {conso}",conso)
print("o total de consoantes e ", cont)
