from random import randint
from socket import NI_NUMERICHOST

numeros = tuple(randint(0, 100) for x in range(20))

for x in range(len(numeros)):
    print(f"{numeros[x]}", end=", ")

print('')

while True:
    busca = int(input("informe o piloto desejado:"))
    if busca == "":
        break
    

    achou = False

    for n in range(len(numeros)):
        if numeros[n] == busca:
            print(f"numero {busca} esta localizado em {n} ")
            achou = True

    if not achou:
        print("o piloto nao foi localizado")
